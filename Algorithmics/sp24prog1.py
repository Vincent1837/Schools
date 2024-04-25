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
def quick_sort(A, p, r, steps):
    def partition(A, p, r, steps):
        i = p - 1
        for j in range(p, r):
            if A[j] <= A[r]:
                i += 1
                A[i], A[j] = A[j], A[i]
                steps += [list(A)]
        A[i + 1], A[r] = A[r], A[i + 1]
        steps += [list(A)]
        return i + 1
    if p < r:
        q = partition(A, p, r, steps)
        quick_sort(A, p, q - 1, steps)
        quick_sort(A, q + 1, r, steps)

# Heap sort
def heap_sort(data, steps):
    n = len(data)
    for i in range(n//2-1, -1, -1):
        heapify(data, n, i, steps)
    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        steps += [list(data)]
        heapify(data, i, 0, steps)
        
def heapify(data, n, i, steps):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and data[l] > data[largest]:
        largest = l
    if r < n and data[r] > data[largest]:
        largest = r
    if largest!= i:
        data[i], data[largest] = data[largest], data[i]
        steps += [list(data)]
        heapify(data, n, largest, steps)

# helper function for removing duplicated elements in steps
def remove_duplicates(lst):
    seen = set()
    result = []
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            result.append(sublist)
            seen.add(sublist_tuple)
    return result


if __name__ == '__main__':
    # generate random data
    import random
    data = random.sample(range(1, 51), 50)
    
    # each step of sorting
    bubble_sort_steps = [list(data)]
    insertion_sort_steps = [list(data)]
    merge_sort_steps = [list(data)]
    quick_sort_steps = [list(data)]
    heap_sort_steps = [list(data)]

    # sort the data and record the steps
    for i in bubble_sort(data.copy()):
        bubble_sort_steps += [list(i)]
        
    for i in insertion_sort(data.copy()):
        insertion_sort_steps += [list(i)]

    merge_sort_data = data.copy()
    merge_sort(merge_sort_data, 0, len(data) - 1, merge_sort_steps)
    merge_sort_steps = remove_duplicates(merge_sort_steps)
        
    quick_sort_data = data.copy()
    quick_sort(quick_sort_data, 0, len(data)-1, quick_sort_steps)
    quick_sort_steps = remove_duplicates(quick_sort_steps)
        
    heap_sort(data.copy(), heap_sort_steps)
        
    # --------------------------------------------------------------------------------
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    
    # initialize the figure
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))
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
    if len(quick_sort_steps) < max_step:
        quick_sort_steps += [quick_sort_steps[-1] for i in range(max_step - len(quick_sort_steps))]
    if len(heap_sort_steps) < max_step:
        heap_sort_steps += [heap_sort_steps[-1] for i in range(max_step - len(heap_sort_steps))]
    # combining the steps
    sorting_steps = [[bubble_sort_steps[i], insertion_sort_steps[i], merge_sort_steps[i], quick_sort_steps[i], heap_sort_steps[i]] for i in range(max_step)]
        
    # animation
    def update(frame):
        for i in range(5):
            for j, rect in enumerate(bars[i]):
                rect.set_height(frame[i][j])
        
    # each frame is a step of sorting
    ani = FuncAnimation(fig, func=update, frames=sorting_steps, interval=100, repeat=False)
    fig.tight_layout()
    fig.canvas.set_window_title('Sorting Algorithms Visualization')
    plt.show()