import random

def dualpivot_partition(arr, left, right, pivot1, pivot2):
    if right - left >= 1:
        k = left + 1
        l = k
        g = right - 1
        while k <= g:
            if arr[k] < pivot1:
                arr[k], arr[l] = arr[l], arr[k]
                l += 1
            elif arr[k] > pivot2:
                while arr[g] > pivot2 and k < g:
                    g -= 1
                arr[k], arr[g] = arr[g], arr[k]
                g -= 1
                if arr[k] < pivot1:
                    arr[k], arr[l] = arr[l], arr[k]
                    l += 1
            k +=1
        l -= 1
        g += 1
        arr[left], arr[l] = arr[l], pivot1
        arr[right], arr[g] = arr[g], pivot2

        return l, g  # Return the indices indicating the boundaries of the partitions
    else:
        return left, right  # If the size is less than 1, return the same indices

def partition(arr, left, right, pivot):
    smaller = left
    equal = left
    larger = right

    while equal <= larger:
        if arr[equal] < pivot:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1

    return smaller, larger

def sesquickselect(arr, k, nu):
    n = len(arr)
    scanned_elements = [0]  # Counter to track scanned elements

    def sesquick(left, right, k):
        if left == right:
            return arr[left]

        scanned_elements[0] += right - left + 1  # Increment number of scanned elements

        i = left + random.randint(0, right - left)  # length of the subarray - 1
        pivot1 = arr[i]

       
        j = left + random.randint(0, right - left)  # length of the subarray - 1
        pivot2 = arr[j]
        
        alpha = k / (right - left + 1)

        pivot1, pivot2 = min(pivot1, pivot2), max(pivot1, pivot2)



        if alpha < nu:
            pivot = pivot1
            small, large = partition(arr, left, right, pivot) # If α < ν we partition the array around the smallest of the two pivots
        elif alpha > 1 - nu:
            pivot = pivot2
            small, large = partition(arr, left, right, pivot) # If α > 1 − ν then we partition the array around the largest of the two pivots
        else:
            small, large = dualpivot_partition(arr, left, right, pivot1, pivot2) # If ν ≤ α ≤ 1 − ν we partition around the two pivots using Yaroslavskiy-BentleyBloch (YBB) dual-pivot partitioning
            if k < small:
                return sesquick(left, small - 1, k)
            elif k <= large:
                return sesquick(small, large, k)
            else:
                return sesquick(large + 1, right, k)

            #print("small:",small)
            #print("large:",large)
            #scanned_elements[0] += (large-small+1)  # Increment number of scanned elements for YBB



        if small <= k <= large:
            return arr[k]
        elif k < small:
            return sesquick(left, small - 1, k)
        else:
            return sesquick(large + 1, right, k)

    # If a non-existing rank is sought
    if k < 0 or k >= n:
        raise ValueError("Index out of range")

    result = sesquick(0, n - 1, k)
    scanned_count = scanned_elements[0]  # Number of scanned elements
    return result, scanned_count

# Example usage:
arr = [3, 6, 2, 9, 1, 5, 7, 8, 4]
k = 3
nu = 0.2

result, scanned_count = sesquickselect(arr, k, nu)
print(f"The {k + 1}th smallest element is: {result}")
print(f"Number of scanned elements: {scanned_count}")
