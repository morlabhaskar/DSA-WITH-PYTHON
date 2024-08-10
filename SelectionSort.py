arr = [4,2,3,1,5,8,6,9,7,10]
def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

res = SelectionSort(arr)
print(res)