# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/5508204456968192

def sort_colors(colors):

    start = 0
    i = 0   # current
    end = len(colors) - 1

    while i <= end:
        if colors[i] == 0:
            colors[start], colors[i] = colors[i], colors[start]
            start += 1
            i += 1
        elif colors[i] == 2:    # not incrementing i is crucial so we can inspect what was switched into current
            colors[end], colors[i] = colors[i], colors[end]
            end -= 1
        else:   # when current is 1
            i += 1

    return colors