def heapyfy(arr, n, i):
    big_root = i
    right = i * 2 + 1
    left = i * 2 + 2
    if right < n and arr[right] > arr[big_root]:
        big_root = right
    if left < n and arr[left] > arr[big_root]:
        big_root = left
    if big_root != i:
        arr[i], arr[big_root] = arr[big_root], arr[i]
        heapyfy(arr, n, big_root)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapyfy(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapyfy(arr, i, 0)  # Восстанавливаем кучу для оставшейся части
