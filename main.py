import time, random, copy, csv

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

def test_algorithms(repeats, size):
    select_times = []
    quick_times = []

    for x in range(repeats):
        unsorted_array = random.sample(range(10000), size)

        select_array = unsorted_array.copy()
        start = time.perf_counter()
        selection_sort(select_array)
        end = time.perf_counter()
        select_times.append(end - start)

        quick_array = unsorted_array.copy()
        start = time.perf_counter()
        quick_sort(quick_array, 0, len(quick_array) - 1)
        end = time.perf_counter()
        quick_times.append(end - start)

    print(f"\nSelection sort minimum time: {min(select_times):.7f}")
    print(f"Selection sort average time: {sum(select_times) / len(select_times):.7f}")
    print(f"Selection sort maximum time: {max(select_times):.7f}")

    print(f"\nQuick sort minimum time: {min(quick_times):.7f}")
    print(f"Quick sort average time: {sum(quick_times) / len(quick_times):.7f}")
    print(f"Quick sort maximum time: {max(quick_times):.7f}")

    with open("timings.csv", "w", newline="") as timings_file:
        writer = csv.writer(timings_file)
        writer.writerow(["Trial", "Selection Sort", "Quick Sort"])

        for trial, (select, quick) in enumerate(zip(select_times, quick_times)):
            writer.writerow([trial+1, f"{select:.7f}", f"{quick:.7f}"])

REPEATS = 20
SIZE = 1000
test_algorithms(REPEATS, SIZE)