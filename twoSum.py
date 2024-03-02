
def two_sum(nums: list, target):
    arr = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                arr.append(i)
                arr.append(j)

    return arr


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
