arr = [4,8,2,1,3,5,7,6,9]

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

print(arr)
k = BubbleSort(arr)
print(k)
