#34. Find First and Last Position of Element in Sorted Array
def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        low=0
        hight = len(nums)-1
        ans = [-1,-1]
        mid = 0
        while low <= hight:
            mid = (low + hight) // 2
            guess = nums[mid]
            if guess == target:
                break
            if guess > target:
                hight = mid - 1
            else: low = mid + 1
        if nums[mid] != target:
            return ans
        ans[1] = mid
        for i in range(mid, len(nums)):
            if nums[i] != target:
                break
            else: ans[1] = i
        ans[0] = mid
        for i in range(mid, -1, -1):
            if nums[i] != target:
                break
            else: ans[0] = i
        return ans
