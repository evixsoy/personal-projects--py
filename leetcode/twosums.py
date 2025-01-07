# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

nums = [3,2,4]
target = 6

def twosums():
    output = []
    for i_index, i in enumerate(nums):
        for y_index, y in enumerate(nums):
            if i +y ==target and i_index != y_index:
                output.append(i_index)
                output.append(y_index)
                return output

print(twosums())  