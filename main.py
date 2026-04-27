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

def test_algorithms(size, trials, repeats):
    setup = """
from __main__ import selection_sort, quick_sort
import random
array = array_2 = [random.randint(0, 100) for x in range(""" + str(size) + """)]
n = len(array)
print(f"Sorting: {array}")
"""

    test_select = """
selection_sort(array)
print(f"Sorted: {array}")
"""
    test_quick = """
quick_sort(array_2, 0, n - 1)
print(f"Sorted: {array_2}")
"""

    select_times = timeit.repeat(stmt=test_select,setup=setup,repeat=repeats,number=trials)
    select_min_time = min(select_times)
    print(f"Selection sort minimum time: {select_min_time/trials:.20f}\n")

    quick_times = timeit.repeat(stmt=test_quick, setup=setup, repeat=repeats, number=trials)
    quick_min_time = min(quick_times)
    print(f"Quick sort minimum time: {quick_min_time / trials:.20f}")

SIZE = 20
TRIALS = 1
REPEATS = 1
test_algorithms(SIZE, TRIALS, REPEATS)