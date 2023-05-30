def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def first_and_last(L, x):
    ekindex = binary_search(L,x)
    left,right = ekindex,ekindex
    if ekindex == -1: return (-1,-1)
    else:
        while L[ekindex]==L[left-1] or L[ekindex]==L[right+1]:
            if L[ekindex] == L[left-1]: left-=1
            if L[ekindex] == L[right+1]: right+=1
        return (left,right)
    
#print(first_and_last([1, 4, 4, 4, 5, 7, 9, 9, 10, 11],9))
            

