#!usr/bin/env python3
import math


def bubble_sort(array, ascending=True):
    """
    Сравниваем два соседних элемента массива, если они стоят не в нужном порядке.
    Проходим по массиву такое количество раз, какое количество элементов он содержит.
    """
    new_arr = array.copy()

    for _ in range(1, len(new_arr)):
        for i in range(1, len(new_arr)):
            if (ascending and new_arr[i-1] > new_arr[i]) or (not ascending and new_arr[i-1] < new_arr[i]):
                # Swap two items if they're not in the order
                new_arr[i], new_arr[i-1] = new_arr[i-1], new_arr[i]

    return new_arr


def gnome_sort(array, ascending=True):
    """
    Сравниваем два соседних элемента массива и сдвигаемся на следующую позицию,
    если элементы стоят в правильном порядке, иначе меняем элементы местами и
    сдвигаемся на одну позицию назад. Выполняем до тех пор, пока позиция не
    будет равна длине исходного массива.
    """
    new_arr = array.copy()
    position = 0
    while position < len(new_arr):
        if (ascending and (position == 0 or new_arr[position] >= new_arr[position-1])) or \
                (not ascending and (position == 0 or new_arr[position] <= new_arr[position-1])):
            position += 1
        else:
            # Swap two items if they're not in the order
            new_arr[position], new_arr[position-1] = new_arr[position-1], new_arr[position]
            position -= 1
    return new_arr


def bucket_sort(array, bucketSize=3, ascending=True):
    """
    Распределяем элементы исходного массива по небольшим спискам (размером <= bucketSize),
    после чего сортируем полученные списки (buckets) по отдельности. После сортировки всех
    списков, объединяем их в один массив.
    """
    new_arr = array.copy()
    if len(new_arr) == 0:
        return new_arr

    # Determine minimum and maximum values
    minValue = new_arr[0]
    maxValue = new_arr[0]
    for i in range(1, len(new_arr)):
        if new_arr[i] < minValue:
            minValue = new_arr[i]
        elif new_arr[i] > maxValue:
            maxValue = new_arr[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(new_arr)):
        buckets[math.floor((new_arr[i] - minValue) / bucketSize)].append(new_arr[i])

    # Sort buckets and place back into input array
    new_arr = []
    for i in range(0, len(buckets)):
        buckets[i] = bubble_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            if ascending:
                new_arr.append(buckets[i][j])
            else:
                new_arr.insert(0, buckets[i][j])

    return new_arr

def default_compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def heapify(array, heap_size, i, compare):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < heap_size and compare(array[left], array[largest]) > 0:
        largest = left
    if right < heap_size and compare(array[right], array[largest]) > 0:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, heap_size, largest, compare)


def build_heap(array, heap_size, compare):
    for i in range(math.floor(len(array) / 2), -1, -1):
        heapify(array, heap_size, i, compare)


def heap_sort(array, compare=default_compare):
    new_arr = array.copy()
    heap_size = len(new_arr)
    build_heap(new_arr, heap_size, compare)
    while heap_size > 1:
        heap_size -= 1
        new_arr[0], new_arr[heap_size] = new_arr[heap_size], new_arr[0]
        heapify(new_arr, heap_size, 0, compare)
    return new_arr


if __name__ == '__main__':
    # Get an array of integers from the user's input
    user_array = [int(i) for i in input().strip().split()]

    print(bubble_sort(user_array, ascending=False))
    print(gnome_sort(user_array, ascending=False))
    print(bucket_sort(user_array, ascending=False))
    print(heap_sort(user_array))
