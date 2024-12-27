import datetime
import sys
from multiprocessing import Process
from threading import Thread
from typing import Any, Callable


def log_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        execution_time = datetime.datetime.now() - start_time
        print(
            f"  [-] Function '{func.__name__}' executed in {execution_time.total_seconds()} seconds."
        )
        return result

    return wrapper


def get_fibonacci_no(n: int = 1) -> int:
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


@log_time
def run_single_thread_task(func: Callable[[Any], Any], input_data: list[Any]) -> None:
    print("[+] Start single thread task...")
    for data in input_data:
        func(data)


@log_time
def run_multi_thread_task(func: Callable[[Any], Any], input_data: list[Any]) -> None:
    print("[+] Start multi thread task...")
    threads = []
    for data in input_data:
        thread = Thread(target=func, args=(data,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


@log_time
def run_multi_processing_task(
        func: Callable[[Any], Any], input_data: list[Any]
) -> None:
    print("[+] Start multi processing task...")
    processes = []
    for data in input_data:
        process = Process(target=func, args=(data,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()




def display_python_info() -> None:
    is_gil_enabled = True
    try:
        is_gil_enabled = sys._is_gil_enabled()
    except AttributeError:
        pass

    print(f"Python version: {sys.version}")
    print(f"Python implementation: {sys.implementation.name}")
    print(f'GIL status: {"Enabled" if is_gil_enabled else "Disabled"}')

def main():
    display_python_info()

    func = get_fibonacci_no
    input_data = [400000] * 3
    run_single_thread_task(func=func, input_data=input_data)
    run_multi_thread_task(func=func, input_data=input_data)
    run_multi_processing_task(func=func, input_data=input_data)


if __name__ == "__main__":
    main()
