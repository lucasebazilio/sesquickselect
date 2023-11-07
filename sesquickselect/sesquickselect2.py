import random


def dualPivotPartition(A, left, right):
    if right - left >= 1:
        pivot1 = A[left]
        pivot2 = A[right]
        k = left + 1
        l = k
        g = right - 1
        while k <= g:
            if A[k] < pivot1:
                A[k], A[l] = A[l], A[k]
                l += 1
            elif A[k] >= pivot2:
                while A[g] > pivot2 and k < g:
                    g -= 1
                A[k], A[g] = A[g], A[k]
                g -= 1
                if A[k] < pivot1:
                    A[k], A[l] = A[l], A[k]
                    l += 1
            k += 1

        l -= 1
        g += 1
        A[left] = A[l]
        A[l] = pivot1
        A[right] = A[g]
        A[g] = pivot2
        return l, g

def partition(arr, left, right, v, alpha):
    pivot = arr[-1] # pivot is the last element of the subarray. If α < ν it will be pivot1. If α > 1-ν it will be pivot2.
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def sesquickselect(arr, k, nu,scanned_elements=None):

    if scanned_elements is None:
        scanned_elements = [0]  # Initialize scanned elements counter only in the first call

    n = len(arr)

    if n == 1:
        return arr[0], scanned_elements[0]  # Base Case: Array Size is 1 -> the sought element is inside the array.

    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    while i == j:     # Pick different pivots at each recursive stage
        j = random.randint(0, n - 1)

    if arr[i] > arr[j]:   # if pivot1 = A[i] > pivot2 = A[j] then swap pivot1 and pivot2
        i, j = j, i

    arr[0], arr[i] = arr[i], arr[0] # Swap: move the pivot1 to the beginning to facilitate partition
    if j == 0:              # prevent the scenario where the same pivot element ends up as both the first and last elements
        j = i
    arr[-1], arr[j] = arr[j], arr[-1] # Swap: move the pivot2 position to the end to facilitate partition

    alpha = float(k) / n # Rank α considering that at each recursive stage the size of the array is smaller

    if alpha < nu:
      arr[0], arr[-1] = arr[-1], arr[0] # Swap because we want to partition around pivot1
      position = partition(arr, 0, n - 1, nu, alpha)
      scanned_elements[0] += n - 1 # we sum n-1
      if k == position:
          return arr[k], scanned_elements[0]

      if k < position:
          return sesquickselect(arr[:position], k, nu,scanned_elements)
      else:
          return sesquickselect(arr[position + 1:], k - position - 1, nu,scanned_elements)

    elif alpha > 1 - nu:
      position = partition(arr, 0, n - 1, nu, alpha)
      scanned_elements[0] += n - 1 # we sum n-1
      if k == position:
          return arr[k], scanned_elements[0]

      if k < position:
          return sesquickselect(arr[:position], k, nu)
      else:
          return sesquickselect(arr[position + 1:], k - position - 1, nu,scanned_elements)

    else:
      scanned_elements[0] += n-1 # we sum (n-1)
      small, large = dualPivotPartition(arr, 0, n - 1)
      scanned_elements[0] += small-2  # we sum (-2) + leftmost part
      if  k == small or k == large:
         return arr[k], scanned_elements[0]

      if k < small:
         return sesquickselect(arr[:small], k, nu,scanned_elements)
      elif small < k < large:
         return sesquickselect(arr[small + 1:large], k - small - 1, nu,scanned_elements)
      else:
         return sesquickselect(arr[large + 1:], k - large - 1, nu,scanned_elements)
    


# Example usage:
arr = [3, 6, 2, 9, 1, 5, 7, 8, 4,10]
k = 3
nu = 0.4

result, scanned_count = sesquickselect(arr, k, nu)
print(f"The {k + 1}th smallest element is: {result}")
print(f"Number of scanned elements: {scanned_count}")
