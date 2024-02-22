"""
CSE 431 HW # 3 Question 1
Implementation of insertion sort and merge sort

Source -
    Project 4 - Hybrid Sorting - Solution Code
    CSE 331 Fall 2022 - Noel Vazquez

"""
import gc
import random
import timeit
import matplotlib.pyplot as plt
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")  # represents generic type
# do_comparison is an optional helper function but HIGHLY  recommended!!!
def do_comparison(first: T, second: T, key: Callable[[T], T], descending: bool) -> bool:
    """
    FILL OUT DOCSTRING
    Takes two values and tells u if it should swap places or not
    :return: bool to perform the sort in descending order when this is True. Defaults to False
    :param: first - first value, second - second value
     key - function which takes an argument of type T and returns new value of first argument
    """
    if key(first) == key(second):
        return False
    if key(first) < key(second):
            if descending == True:
                return True
            else:
                return False
    else:
        if descending == True:
            return False
        else:
            return True
    pass

def insertion_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                   descending: bool = False) -> None:
    """
    Given a list of values, sort that list in-place using the insertion sort algorithm
    and perform the sort in descending order if descending is True.
    :return: none
    :param:
    data - List of items to be sorted
    key - function which takes an argument of type T and returns new value of first argument
    descending - Perform the sort in descending order when this is True, otherwise false.

    """

    for i in range(1, len(data)):
        j = i - 1
        k = i
        while(0 < k):
            if (not do_comparison(data[j], data[k], key, descending)):
                break
            temp = data[k]
            data[k] = data[j]
            data[j] = temp
            j -= 1
            k -= 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def generate_random_data(size):
    return [random.randint(1, 100000) for _ in range(size)]


def plot_results(sizes, insertion_runtimes, merge_runtimes):
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, insertion_runtimes, marker='o', label='Insertion Sort')
    plt.plot(sizes, merge_runtimes, marker='s', label='Merge Sort')
    plt.xlabel('Number of Integers')
    plt.ylabel('Runtime (seconds)')
    plt.title('Sorting Algorithm Runtime Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    sizes = range(1000, 11000, 1000)
    insertion_runtimes = []
    merge_runtimes = []

    for size in sizes:
        data = generate_random_data(size)

        # Prepare the sort functions for timing
        insertion_sort_setup = f"from __main__ import insertion_sort; import random; data = {data}"
        merge_sort_setup = f"from __main__ import merge_sort; import random; data = {data}"

        # Time Insertion Sort using timeit
        insertion_time = timeit.timeit('insertion_sort(data[:])', setup=insertion_sort_setup, number=1)
        insertion_runtimes.append(insertion_time)

        # Time Merge Sort using timeit
        merge_time = timeit.timeit('merge_sort(data[:])', setup=merge_sort_setup, number=1)
        merge_runtimes.append(merge_time)

        print(f"Size: {size}, Insertion Sort Time: {insertion_runtimes[-1]}, Merge Sort Time: {merge_runtimes[-1]}")

    plot_results(list(sizes), insertion_runtimes, merge_runtimes)


if __name__ == "__main__":
    main()