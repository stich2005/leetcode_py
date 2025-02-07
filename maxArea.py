#11. Container With Most Water
def maxArea(self, height: List[int]) -> int:
        l_point = 0
        r_point = len(height)-1
        ans = 0
        while r_point > l_point:
            if (r_point-l_point)*(height[r_point] if height[r_point] < height[l_point] else height[l_point]) > ans:
                ans = (r_point-l_point)*(height[r_point] if height[r_point] < height[l_point] else height[l_point])
            if height[r_point] > height[l_point]:
                l_point += 1
            else:
                r_point -= 1
        return ans
