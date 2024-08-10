#ITERATION MOTHOD

# arr = [2,4,5,6,7,9,10,13,15,17,19,20]
# x = 20
# def binarySearch(arr,x,low,high):
#     while low <= high:
#         mid = low + (high-low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = low + 1
#         else:
#             high = high - 1
#     return -1 

# res = binarySearch(arr,x,0,len(arr)-1)

# if res == -1:
#     print("Element is Not Found")
# else:
#     print(f"Element in the array index of : {res}")






# RECURSIVE METHOD

arr = [2,4,5,6,7,9,10,13,15,17,19,20]
x = 5
def binarySearch(arr,x,low,high):
    if low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr,x,mid+1,high)
        else:
            return binarySearch(arr,x,low,mid-1)
    return -1 

res = binarySearch(arr,x,0,len(arr)-1)

if res == -1:
    print("Element is Not Found")
else:
    print(f"Element in the array index of : {res}")