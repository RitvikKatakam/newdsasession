def container_with_most_water(height):
    n = len(height)
    l,r = 0,n-1
    maxArea = 0
    while l<r:
        width = r - l
        h = min(height[l],height[r])
        area = width*h
        maxArea = max(maxArea,area)
        
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return maxArea

#example usage
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(container_with_most_water(height))
    # time complexity: O(n)
    # space complexity: O(1)