# binary search - recursion
def binary_r(array, target, start, end):
    mid  = start+ + end // 2
    if array[mid] == target:
        return mid
    elif array[mid] >= target:
        return binary_r(array,target,start,mid-1)
    else:
        return binary_r(array, target, mid+1, end)

# binary search - iteration
def binary_i(array, target, start, end):
    mid = start + end // 2
    while start >= end:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

