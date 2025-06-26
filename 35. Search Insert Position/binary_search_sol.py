class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                head = mid + 1
            else:
                tail = mid - 1
        return head