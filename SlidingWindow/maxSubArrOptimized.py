
#solving the problem in Big O(n) time complexity
arr = arr = [1,3,5,2,7,4]
k = 3

def maxSum(arr,k):
    windowSum = 0
    maxSum = 0
    maxSubArr = [] #we need to return max subarray and maxSum
    window_start = 0
    for window_end in range(len(arr)): 
        
        windowSum += arr[window_end]
        
        #after calculating sum of first elements of size K this loop will run everytime
        if window_end >= k  - 1: # now we iterated till the elements in "k" sequence
            #we did k - 1 cause window_end starts at 0
            #and added the sum till Kth sequence we will do comparsions now
            
            if windowSum > maxSum:
                maxSum = windowSum
                maxSubArr = arr[window_start:window_end+1] 
                # did window_end + 1 due slice properties
                
            #now we increment window_start as to get to new subsequence of size k
            #and subtract the first element of the  current subsequence so the remaning sum can be added to 
            # Remove the element going out of the window
            
            windowSum -= arr[window_start]
            window_start+=1   #moving our window array ahead for maxSubArr
    
    return maxSum , maxSubArr
             
        
        
        
    
    
