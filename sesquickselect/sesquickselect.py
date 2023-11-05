import random

def dualpivot_partition(arr, low, high, pivot1, pivot2):

    i = low
    left = low
    right = high

    while i <= right:
        if arr[i] < pivot1:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] > pivot2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

    i = left
    while i < right:
        if arr[i] == pivot1:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == pivot2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

    return left - 1, right + 1


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

        #print("begin:",arr)
        scanned_elements[0] += right - left + 1  # Increment number of scanned elements
        if right - left > 0:
          i = random.randint(left, right - 1)
          j = random.randint(i + 1, right)
          pivot1 = arr[i]
          pivot2 = arr[j]
        else:
            pivot1 = arr[left]
            pivot2 = arr[right]
        
        #alpha = k / (right - left + 1)
        alpha = (k - left) / (right - left + 1)
        pivot1, pivot2 = min(pivot1, pivot2), max(pivot1, pivot2)

        #print("pivot1:",pivot1)
        #print("pivot2:",pivot2)



        if alpha < nu:
            pivot = pivot1
            
            small, large = partition(arr, left, right, pivot) # If α < ν we partition the array around the smallest of the two pivots
            #print("part1")

            if k <= small:
              return sesquick(left, small, k)
            elif k >= large:
              return sesquick(large, right, k)
            else:
              return arr[k]

        elif alpha > 1 - nu:
            pivot = pivot2
            
            small, large = partition(arr, left, right, pivot) # If α > 1 − ν then we partition the array around the largest of the two pivots
            #print("part2")

            if small < k < large:
                return arr[k]
            elif k < small:
               return sesquick(left, small-1, k)
            else:
              return sesquick(large, right, k)

        else:
            small, large = dualpivot_partition(arr, left, right,pivot1,pivot2) # If ν ≤ α ≤ 1 − ν we partition around the two pivots using Yaroslavskiy-BentleyBloch (YBB) dual-pivot partitioning
            #print("dual")
            if small <= k <= large:
              return sesquick(small,large,k)
            elif k < small:
              return sesquick(left, small - 1, k)
            else:
              return sesquick(large + 1, right, k)


            #print("small:",small)
            #print("large:",large)
            #scanned_elements[0] += (large-small+1)  # Increment number of scanned elements for YBB


        #print("end:",arr)


    # If a non-existing rank is sought
    if k < 0 or k >= n:
        raise ValueError("Index out of range")

    result = sesquick(0, n - 1, k)
    scanned_count = scanned_elements[0]  # Number of scanned elements
    return result, scanned_count

# Example usage:
arr = [3, 6, 2, 9, 1, 5, 7, 8, 4,10]
k = 3
nu = 0.3

result, scanned_count = sesquickselect(arr, k, nu)
print(f"The {k + 1}th smallest element is: {result}")
print(f"Number of scanned elements: {scanned_count}")
