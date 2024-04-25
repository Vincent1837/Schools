

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


import random
arr = random.sample(range(1, 51), 50)
merge_sort_steps = [list(arr)]
merge_sort(arr, 0, len(arr) - 1, merge_sort_steps)
    
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
   
# remove steps with the same elements
merge_sort_steps = [x for x in merge_sort_steps if len(set(x)) == len(x)]

print(len(merge_sort_steps))


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

