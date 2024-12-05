def selection_sort(arr):
    comparisons, movements = 0, 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            movements += 2
    return arr, comparisons, movements


def insertion_sort(arr):
    comparisons, movements = 0, 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            movements += 1
            j -= 1
        comparisons += 1  # 마지막 비교
        arr[j + 1] = key
        movements += 1
    return arr, comparisons, movements


def bubble_sort(arr):
    comparisons, movements = 0, 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 2
    return arr, comparisons, movements


def shell_sort(arr):
    comparisons, movements = 0, 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                movements += 1
                j -= gap
            arr[j] = temp
            movements += 1
        gap //= 2
    return arr, comparisons, movements


def heap_sort(arr):
    comparisons, movements = 0, 0

    def heapify(n, i):
        nonlocal comparisons, movements
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            movements += 2
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        movements += 2
        heapify(i, 0)
    return arr, comparisons, movements


def merge_sort(arr):
    comparisons, movements = 0, 0

    def merge(left, right):
        nonlocal comparisons, movements
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                movements += 1
                i += 1
            else:
                result.append(right[j])
                movements += 1
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        movements += len(left[i:]) + len(right[j:])
        return result

    if len(arr) <= 1:
        return arr, comparisons, movements

    mid = len(arr) // 2
    left, c1, m1 = merge_sort(arr[:mid])
    right, c2, m2 = merge_sort(arr[mid:])
    comparisons += c1 + c2
    movements += m1 + m2
    return merge(left, right), comparisons, movements


def quick_sort(arr):
    comparisons, movements = 0, 0

    def partition(low, high):
        nonlocal comparisons, movements
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                movements += 2
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        movements += 2
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(arr) - 1)
    return arr, comparisons, movements


def radix_sort(arr):
    movements, comparisons = 0, 0
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        count = [0] * 10
        output = [0] * len(arr)
        for i in arr:
            count[(i // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(arr) - 1, -1, -1):
            output[count[(arr[i] // exp) % 10] - 1] = arr[i]
            count[(arr[i] // exp) % 10] -= 1
            movements += 1
        for i in range(len(arr)):
            arr[i] = output[i]
            movements += 1
        exp *= 10
    return arr, comparisons, movements


def sort_and_display(arr, algorithm):
    sort_functions = {
        "SEL": selection_sort,
        "INS": insertion_sort,
        "BUB": bubble_sort,
        "SHE": shell_sort,
        "HEA": heap_sort,
        "MER": merge_sort,
        "QUI": quick_sort,
        "RAD": radix_sort,
    }
    if algorithm in sort_functions:
        sorted_arr, comparisons, movements = sort_functions[algorithm](arr.copy())
        print(f">> Sorted: {', '.join(map(str, sorted_arr))}")
        print(f">> Number of Comparisons: {comparisons}")
        print(f">> Number of Data Movements: {movements}")
    else:
        print("Invalid algorithm selected.")

def main():
    while True:
        data_input = input("* Please input a data list: ")
        arr = list(map(int, data_input.split(',')))
        print(" * Target Sorting Algorithm List")
        print(" Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
        algorithm = input(" * Select sorting algorithm: ").strip().upper()
        sort_and_display(arr, algorithm)
        
        exit_choice = input("Press 'p' to exit or any other key to continue: ").strip().lower()
        if exit_choice == 'p':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
