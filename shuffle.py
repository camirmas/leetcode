from random import randint

def shuffle(nums):
    len_nums = len(nums)

    for i, num in enumerate(nums):
        rand_i = randint(i, len_nums - 1)
        if i != rand_i:
            nums[i], nums[rand_i] = nums[rand_i], nums[i]

    return nums
