nums = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]
max_index = len(nums)-1
for i in range(0, len(nums),1):
    print(f"from left {nums[i][i]}")
    print(f"from right {nums[i][max_index - i]}")
