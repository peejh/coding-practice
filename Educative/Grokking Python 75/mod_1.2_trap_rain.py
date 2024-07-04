# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/6243637528756224

def rain_water(heights):

    left = 0
    right = len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    total_rain = 0

    while left <= right:
        # the difference with official solution is that this continues to calculate
        # rain water even while the maxes are equal and only switches when one side
        # is higher than the other
        # this makes more sense visually
        if left_max <= right_max:
            if heights[left] < left_max:
                total_rain += left_max - heights[left]
            else:
                left_max = heights[left]
            left += 1
        elif right_max <= left_max:
            if heights[right] < right_max:
                total_rain += right_max - heights[right]
            else:
                right_max = heights[right]
            right -= 1

    return total_rain