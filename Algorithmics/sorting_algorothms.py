import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Bubble sort
def bubble_sort(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i] # swap
                swapped = True
                yield data
        if not swapped:
            break

# Insetrtion sort
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i-1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j] # shift
            j -= 1
            yield data
        data[j+1] = key # shift
        yield data

# Merge sort
def merge_sort(A, p, r, steps):
    if p >= r:
        return
    q = ((p + r) / 2).__floor__()
    merge_sort(A, p, q, steps)
    merge_sort(A, q + 1, r, steps)
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    i, j, k = 0, 0, p
    while i <= q - p and j <= r - q - 1:
        if L[i] <= R[j]:
            A[k] = L[i]
            steps += [list(A)]
            i += 1
        else:
            A[k] = R[j]
            steps += [list(A)]
            j += 1
        k += 1
    while i <= q - p:
        A[k] = L[i]
        steps += [list(A)]
        i += 1
        k += 1
    while j <= r - q - 1:
        A[k] = R[j]
        steps += [list(A)]
        j += 1
        k += 1 

# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        yield arr
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    yield from quick_sort(left)
    yield middle
    yield from quick_sort(right)

# Heap sort
def heap_sort(data):
    n = len(data)
    for i in range(n//2-1, -1, -1):
        heapify(data, n, i)
    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)
        yield data
        
# Heapify
def heapify(data, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and data[l] > data[largest]:
        largest = l
    if r < n and data[r] > data[largest]:
        largest = r
    if largest!= i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


if __name__ == '__main__':
    
    data = random.sample(range(1, 51), 50)

    bubble_sort_steps = [list(data)]
    insertion_sort_steps = [list(data)]
    merge_sort_steps = [list(data)]
    quick_sort_steps = [list(data)]
    heap_sort_steps = [list(data)]

    
    for i in bubble_sort(data.copy()):
        bubble_sort_steps += [list(i)]
        
    for i in insertion_sort(data.copy()):
        insertion_sort_steps += [list(i)]

    merge_sort_data = data.copy()
    merge_sort(merge_sort_data, 0, len(merge_sort_data) - 1, merge_sort_steps)
    # remove duplicates
    def remove_duplicates(lst):
        seen = set()
        result = []
        for sublist in lst:
            sublist_tuple = tuple(sublist)
            if sublist_tuple not in seen:
                result.append(sublist)
                seen.add(sublist_tuple)
        return result
    merge_sort_steps = remove_duplicates(merge_sort_steps)
        
    for i in quick_sort(data.copy()):
        quick_sort_steps += [list(i)]
        
    for i in heap_sort(data.copy()):
        heap_sort_steps += [list(i)]
        
    """ for i in merge_sort_steps:
        print(i) """
        
    # ----------------------------------------------------------------    
    # initialize the figure
    fig, axes = plt.subplots(1, 5, figsize=(15, 4))
    bars = []
    algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
    for i, ax in enumerate(axes):
        ax.set_title(algorithms[i])
        ax.set_ylim(top=55)
        ax.set(xticks=[], yticks=[])
        ax.autoscale()
        bars.append(ax.bar(range(len(data)) , data, align='edge', color='blue'))

    # make the steps have the same length
    max_step = max(len(bubble_sort_steps), len(insertion_sort_steps))
    if len(bubble_sort_steps) < max_step:
        bubble_sort_steps += [bubble_sort_steps[-1] for i in range(max_step - len(bubble_sort_steps))]
    if len(insertion_sort_steps) < max_step:
        insertion_sort_steps += [insertion_sort_steps[-1] for i in range(max_step - len(insertion_sort_steps))]
    if len(merge_sort_steps) < max_step:
        merge_sort_steps += [merge_sort_steps[-1] for i in range(max_step - len(merge_sort_steps))] 
    # combining the steps
    sorting_steps = [[bubble_sort_steps[i], insertion_sort_steps[i], merge_sort_steps[i]] for i in range(max_step)]

    # animation
    def update(frame):
        for i, rect in enumerate(bars[0]):
            rect.set_height(frame[0][i])
        for i, rect in enumerate(bars[1]):
            rect.set_height(frame[1][i])
        for i, rect in enumerate(bars[2]):
            rect.set_height(frame[2][i])
        
    ani = FuncAnimation(fig, func=update, frames=sorting_steps, interval=1, repeat=False)
    plt.show()