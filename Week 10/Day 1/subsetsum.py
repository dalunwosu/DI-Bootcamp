def subsetsum(numbers: list, target: int) -> bool:
    for i in range (len(numbers)-1):
        j = i+1
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return f"{True} The numbers are: {numbers[i]} and {numbers[j]}"
    return False
        
def sortsubsetsum(numbers: list, target: int):
    numbers = sorted(numbers)
    left = 0
    right = len(numbers)-1

    while right>left:
        if (numbers[left] + numbers[right]== target):
            return f"{True} The numbers are: {numbers[left]} and {numbers[right]}"
        elif (nums[left]+ nums[right]<target):
            left+= 1
        else:
            right -=1
    return False

def subsetsum_hashtable(nums, target):
    hashtable = {}
    for i in range(len(nums)):  # n actions
        current_number = nums[i]
        hashtable[current_number] = 0

    for i in range(len(nums)):  # n actions
        number_to_find = target - nums[i]
        if number_to_find in hashtable:
            return True
    return False


nums = [12, -7, 20, 1, 4, -10, -1]

print(subsetsum_hashtable(nums, 1))
print(subsetsum_hashtable(nums, 2))
print(subsetsum_hashtable(nums, 3)) 
print(subsetsum_hashtable(nums, 4)) 