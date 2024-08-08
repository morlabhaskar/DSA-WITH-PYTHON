arr = [2,5,4,6,9,8,7,2,3,]
n = len(arr)
x = 1

def LinearSearch(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

res = LinearSearch(arr,n,x)
if res == -1:
    print("Element is Not Found")
else:
    print(f"Element found at Index : {res}")     #string formating  method