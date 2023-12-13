import random

def dualPivotPartition(arr, left, right, scanned_elements):
    if right - left >= 1:
        pivot1 = arr[left]
        pivot2 = arr[right]
        k = left + 1
        l = k
        g = right - 1
        while k <= g:
            if arr[k] < pivot1:
                arr[k], arr[l] = arr[l], arr[k]
                l += 1
            elif arr[k] >= pivot2:
                while arr[g] > pivot2 and k < g:
                    g -= 1
                arr[k], arr[g] = arr[g], arr[k]
                g -= 1
                if arr[k] < pivot1:
                    arr[k], arr[l] = arr[l], arr[k]
                    l += 1
            k += 1

        l -= 1
        g += 1
        arr[left] = arr[l]
        arr[l] = pivot1
        arr[right] = arr[g]
        arr[g] = pivot2
        return l, g

def partition(arr, left, right, nu, alpha, scanned_elements):
    if alpha < nu:
        arr[0], arr[-1] = arr[-1], arr[0]

    pivot = arr[-1]
    position = left
    j = left
    while j < right:
        if arr[j] <= pivot:
            arr[position], arr[j] = arr[j], arr[position]
            position += 1
        j += 1
    arr[position], arr[right] = arr[right], arr[position]
    return position


def sesquickselect(arr, k, nu, scanned_elements=None):
    if scanned_elements is None:
        scanned_elements = [0]  # Initialize scanned elements counter only in the first call

    n = len(arr)
    if n == 1:
        return arr[0], scanned_elements[0]  # If the array size is 1, return element and scanned count

    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    while i == j:
        j = random.randint(0, n - 1)
        
        

    if arr[i] > arr[j]:
        i, j = j, i

    arr[0], arr[i] = arr[i], arr[0]
    if j == 0:
        j = i
    arr[-1], arr[j] = arr[j], arr[-1]

    alpha = float(k) / n

    if alpha < nu or alpha > 1 - nu:
        position = partition(arr, 0, n - 1, nu, alpha, scanned_elements)
        scanned_elements[0] += n - 1  # we sum n-1
        if k == position:
            return arr[k], scanned_elements[0]

        if k < position:
            return sesquickselect(arr[:position], k, nu, scanned_elements)
        else:
            return sesquickselect(arr[position + 1:], k - position - 1, nu, scanned_elements)

    else:
        scanned_elements[0] += n-1  # we sum (n-1)
        small, large = dualPivotPartition(arr, 0, n - 1, scanned_elements)
        scanned_elements[0] += small-2  # we sum (-2) + leftmost part
        if small == k or large == k:
            return arr[k], scanned_elements[0]

        if k < small:
            return sesquickselect(arr[:small], k, nu, scanned_elements)
        elif small < k < large:
            return sesquickselect(arr[small + 1:large], k - small - 1, nu, scanned_elements)
        else:
            return sesquickselect(arr[large + 1:], k - large - 1, nu, scanned_elements)


# Example usage:
arr = [3, 6, 2, 9, 1, 5, 7, 8, 4, 10]
k = 6
nu = 0.1

result, scanned_count = sesquickselect(arr, k, nu)
print(f"The {k + 1}th smallest element is: {result}")
print(f"Number of scanned elements: {scanned_count}")
