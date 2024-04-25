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


import random
arr = random.sample(range(1, 11), 10)

quick_sort_steps = [list(arr)]


quick_sort(arr, 0, len(arr) - 1, quick_sort_steps)

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

quick_sort_steps = remove_duplicates(quick_sort_steps)


# remove steps with the same elements


# from sorting_algorothms import merge_sort

# Example usage:
""" arr = [38, 27, 43, 3, 9, 82, 10]
print("Initial array:", arr)
print("Sorted array:")
for sorted_arr in merge_sort(arr):
    print(sorted_arr) """


""" 
[27, 38, 43][3, 9, 10, 82]
[0 ,  0,  0, 0, 0,  0,  0]

[27, 38, 43, 3, 9, 10, 82]
[3, 27, 38, 43, 9, 10, 82]
[3, 9, 27, 38, 43, 10, 82]
[3, 9, 10, 27, 38, 43, 82] """

