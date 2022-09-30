import sys

n, m = map(int, sys.stdin.readline().split())

nums = list()
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums = sorted(nums)

left = 0
right = 0
sum_num = 0
answer = float('inf')

while left < len(nums) - 1 and right <= len(nums) - 1:
    sum_num = nums[right] - nums[left]
    if sum_num >= m:
        answer = min(answer , sum_num)
        left += 1
        right = left
        continue    
    right += 1


print(answer)