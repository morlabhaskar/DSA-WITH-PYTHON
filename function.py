
def Und(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            pairs.append(f"{arr[i]},{arr[j]}")
    return pairs
arr = [2,3,4,2,4,6]
res = Und(arr)
print(res)
