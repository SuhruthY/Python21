import random

nums = []
# Generate random numbers
for num in range(100):
    num = random.randrange(1,101)
    nums.append(num)

# Sorting the generated list
nums = sorted(nums)

# Creating binary search
def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    while(first <= last and not found):
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


# Testing the binary search function
res_lst =[ binary_search(nums, 45),
           binary_search([1,4,6,9,2,3,5,9], 4),
           binary_search(nums, 5) ]

for res in res_lst:
    if res == True:
        print("I found it!")
    else:
        print("I can't, sorry!")
