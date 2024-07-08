import os
import time
from threading_search import multithreading_search
from multiprocessing_search import multiprocessing_search


def load_files(path):
    return [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]


def main():
    files = load_files("files")
    keywords = ["Proglib", "ресурс", "кількість", "eeeee"]

    # Вимірювання часу для багатопотокового підходу
    start_time = time.time()
    results_threading = multithreading_search(files, keywords)
    end_time = time.time()
    print(f"Threading approach took {end_time - start_time} seconds")
    print(f"Results (Threading): {results_threading}")

    # Вимірювання часу для багатопроцесорного підходу
    start_time = time.time()
    results_multiprocessing = multiprocessing_search(files, keywords)
    end_time = time.time()
    print(f"Multiprocessing approach took {end_time - start_time} seconds")
    print(f"Results (Multiprocessing): {results_multiprocessing}")


if __name__ == "__main__":
    main()
