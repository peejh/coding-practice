# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/6650704546627584

# semi-naive approach
def container_with_most_water(height):
    # find the index of the tallest pillar
    max_idx = height.index(max(height))
    most_water = 0
    
    # in each iteration, calculate the amount of water from the current pillar to the max pillar
    for i in range(len(height)):
        if i == max_idx:
            continue
        curr_water = height[i] * abs(max_idx - i)
        most_water = max(most_water, curr_water)
    
    return most_water

# using 2 pointers
def container_with_most_water2(height):
    start = 0
    end = len(height) - 1
    most_water = 0
    while start < end:
        curr_water = (min(height[start], height[end])) * (end - start)
        most_water = max(most_water, curr_water)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return most_water