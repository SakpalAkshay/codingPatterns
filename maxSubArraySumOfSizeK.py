arr = [1,3,5,2,7,4]
k = 3

hashSet ={}
def maxSum(arr,k):
    max = 0
    
    for i in range(len(arr)):
        sum = 0
        subArr = []
        for j in range(i,min(len(arr),i+k)):
            sum+= arr[j]
            subArr.append(arr[j])
        hashSet[sum] = subArr
        print(hashSet)
        if sum > max:
            max = sum
        print(max)
    if max in hashSet:
        return max, hashSet[max]
    else:
        return False
maxVal, subarr = maxSum(arr, k)
print(maxVal, subarr)
