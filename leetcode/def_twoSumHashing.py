def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print(complement)
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]

# Driver Code
num_arr = [4, 4, 1, 8]
pair_sum = 8
  
# Calling function
twoSumHashing(num_arr, pair_sum)