#1351. Count Negative Numbers in a Sorted Matrix
def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            low=0
            hight = len(grid[0])-1
            while low <= hight:
                if grid[i][0] < 0:
                    count += len(grid[0])
                    break
                if grid[i][len(grid[0])-1] >= 0:
                    break
                mid = (low + hight) // 2
                if grid[i][mid] >= 0 and grid[i][mid+1] < 0:
                    count += (len(grid[0])-mid-1)
                if grid[i][mid] < 0:
                    hight = mid - 1
                else: low = mid + 1
        return count
