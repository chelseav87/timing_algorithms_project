import random

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

size = 10
arr = [random.randint(0,100) for i in range(size)]
array = [random.randint(0,100) for j in range(size)]


# selection sort; iterative implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):

        # Assume the current position holds the minimum element
        min_idx = i

        # Iterate through the unsorted portion to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j

        # Move minimum element to its correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    print("Original array: ", end="")
    print_array(arr)

    selection_sort(arr)

    print("Sorted array: ", end="")
    print_array(arr)


# quick sort; using lomuto partition algorithm

def partition(array, low, high):
    # choose the pivot
    pivot = array[high]

    # index of smaller element and indicates the right position of pivot found so far
    i = low - 1

    # traverse array and move all smaller elements to the left side. Elements from low to i are smaller after every iteration
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)

    # move pivot after smaller elements and return its position
    swap(array, i + 1, high)
    return i + 1

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def quick_sort(array, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(array, low, high)

        # recursion calls for smaller elements and greater or equal elements
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

if __name__ == "__main__":
    n = len(array)

    print("\nOriginal array: ", end="")
    print_array(array)

    quick_sort(array, 0, n - 1)

    print("Sorted array: ", end="")
    print_array(array)