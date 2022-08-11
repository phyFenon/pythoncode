'''
This is the function of quicksort method to arrane a list from a ascending order.
The orginal spirit is the recursive condition.
'''
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[]
        greater=[]
        for val in array[1::]:
            if val<=pivot:
                less.append(val)
            else:
                greater.append(val)
        return quicksort(less)+[pivot]+quicksort(greater)


print(quicksort([3,4,1,3,6,0,0.1]))
print(quicksort([0.1,100,20,3.6,6.9,20,0.01]))