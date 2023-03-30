def longest_sequence_old(nums: list) -> int:
    nums = sorted(nums)
    biggest_sequence = 0
    current_sequence = 1

    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            current_sequence += 1
        else:
            if current_sequence>biggest_sequence:
                biggest_sequence = current_sequence
            current_sequence = 1

    return biggest_sequence

def longest_sequence(nums: list) -> int:
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
nums = [6, 4, 100, 5, 200, 2, 3]
print(longest_sequence(nums))