import timeit

def selection_sort(array):  # iterative implementation
    n = len(array)
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):    # lomuto partition algorithm
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)

    swap(array, i + 1, high)
    return i + 1

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

import random

unsorted_array = [random.randint(0, 100) for x in range(5000)]

def test_algorithms(trials, repeats):
    setup = """
from __main__ import selection_sort, quick_sort, unsorted_array
import random, copy

select_array = quick_array = copy.deepcopy(unsorted_array)

n = len(unsorted_array)
#print(f"Sorting: {unsorted_array}")
"""

    test_select = """
selection_sort(select_array)
#print(f"Sorted: {select_array}")
"""
    test_quick = """
quick_sort(select_array, 0, n - 1)
#print(f"Sorted: {select_array}")
"""

    select_times = timeit.repeat(stmt=test_select,setup=setup,repeat=repeats,number=trials)
    print(f"\nSelection sort minimum time: {min(select_times) / trials:.20f}")
    print(f"Selection sort average time: {(sum(select_times) / len(select_times)) / trials:.20f}")
    print(f"Selection sort maximum time: {max(select_times) / trials:.20f}")

    quick_times = timeit.repeat(stmt=test_quick, setup=setup, repeat=repeats, number=trials)
    print(f"\nQuick sort minimum time: {min(quick_times) / trials:.20f}")
    print(f"Quick sort average time: {(sum(quick_times) / len(quick_times)) / trials:.20f}")
    print(f"Quick sort maximum time: {max(quick_times) / trials:.20f}")

TRIALS = 1
REPEATS = 10
test_algorithms(TRIALS, REPEATS)