def merge_Sort(arr,n):
    temp_arr=[0]*n
    return _mergesort(arr,temp_arr,0,n-1)


def _mergesort(arr,temp_arr,left,right):
    count=0
    if left<right:
        mid=(left+right)//2
        count+=_mergesort(arr,temp_arr,left,mid)
        count+=_mergesort(arr,temp_arr,mid+1,right)
        count+=merge(arr,temp_arr,left,mid,right)
    return count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0
    while i<=mid and j <=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            k+=1
            i+=1

        else:
            temp_arr[k] = arr[j]
            count+=(mid-i)+1
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

            # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

            # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return count


arr = [1, 20, 6, 4, 5]
n = len(arr)
result = merge_Sort(arr, n)
print("Number of inversions are", result)



