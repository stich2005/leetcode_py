#35. Search insert position
def searchInsert(self, nums: List[int], target: int) -> int:
        if target == 0 and nums[0]>target:
            return 0
        low=0
        hight = len(nums)-1
        while low <= hight:
            mid = (low + hight) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                hight = mid - 1
            else: low = mid + 1
        if nums[hight] < target:
            return hight+1
        if nums[low] > target and low > 0:     
            return low-1
        else: return 0
