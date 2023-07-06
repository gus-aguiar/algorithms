def find_duplicate(nums):
    nums.sort()
    if len(nums) == 0 or len(nums) == 1:
        return False
    for i in range(len(nums) - 1):
        if not isinstance(nums[i], (int, float)) or nums[i] < 1:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
