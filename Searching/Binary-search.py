def binary(element,arr,l,r):
    if r >= l:    
        mid = l + (r - l) // 2
        
        if arr[mid] == x:
            return mid
        
        elif(arr[mid] > x):
            return binary(element,arr,l,mid-1)

        else:
            return binary(element,arr,mid+1,r)
    else:
        return -1


arr = [1,2,3,4,5,6,7,8,9]
x = 7

print(binary(x,arr,0,len(arr)-1))



# O(log n)

# O(log N) basically means time goes up linearly while the n goes up exponentially. 
# So if it takes 1 second to compute 10 elements, it will take 2 seconds to compute 100 elements, 
# 3 seconds to compute 1000 elements, and so on