import multiprocessing


def search_keywords_in_files_multiprocessing(files, keywords, queue):
    results = {}
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        if keyword not in results:
                            results[keyword] = []
                        results[keyword].append(file)
        except Exception as e:
            print(f"Error processing file {file}: {e}")
    queue.put(results)


def multiprocessing_search(files, keywords):
    results = {}
    processes = []
    n_processes = 4
    chunk_size = len(files) // n_processes
    queue = multiprocessing.Queue()

    for i in range(n_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < n_processes - 1 else len(files)
        process = multiprocessing.Process(
            target=search_keywords_in_files_multiprocessing,
            args=(files[start:end], keywords, queue),
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        result = queue.get()
        for key, value in result.items():
            if key not in results:
                results[key] = []
            results[key].extend(value)

    return results
