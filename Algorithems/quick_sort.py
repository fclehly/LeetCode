from typing import List

def partition(a: List, p: int, r: int):
    x = a[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r - 1] = a[r - 1], a[i + 1]
    return i + 1

def quick_sort(a: List, p: int, r: int) -> List:
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    return a

print(quick_sort([3, 5, 2, 4, 1], 0, 5))