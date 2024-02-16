arr = [1,7,9,11,13,17]
k = 3 

def average_of_subarray(arr,k):
    windowSum = 0
    windowStart = 0 #for moving the array
    avgArr = []
    for window_variable in range(len(arr)):
        avg = 0
        windowSum += arr[window_variable]
        
        if window_variable >= k - 1: #we so in this condition after we have sum of first k size element
            avg = windowSum // k
            avgArr.append(avg)
            
            windowSum -= arr[windowStart] #so that add next element for next window 
            windowStart+=1 #moving our window by 1 => the new element gets added in next iteration
            
    return avgArr

avg = average_of_subarray(arr,k)
print(avg)        
