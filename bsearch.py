#704. Binary search
def search(self, nums: List[int], target: int) -> int:
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
        return -1
