import threading


def search_keywords_in_files(files, keywords, results):
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


def multithreading_search(files, keywords):
    results = {}
    threads = []
    n_threads = 4
    chunk_size = len(files) // n_threads

    for i in range(n_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < n_threads - 1 else len(files)
        thread = threading.Thread(
            target=search_keywords_in_files, args=(files[start:end], keywords, results)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
