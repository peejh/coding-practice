# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/6524819373948928

def largest_rectangle_naive(heights):
    max_area = 0
    for i, curr in enumerate(heights):
        i_area = curr
        left = i - 1
        while left >= 0:
            if heights[left] >= curr:
                i_area += curr
            else:
                break
            left -= 1
        right = i + 1
        while right < len(heights):
            if heights[right] >= curr:
                i_area += curr
            else:
                break
            right += 1
        max_area = max(max_area, i_area)
    return max_area

def largest_rectangle(heights):
    # constraints indicate that there's at least 1 element in the list
    # this is needed for now to avoid out of index error later on
    if len(heights) == 1:
        return heights[0]

    max_area = 0
    stack = [heights[0], 1] # for tracking heights and their length

    # STEP 1: traverse through heights list
    for h in heights[1:]:
        # h is current height
        # stack[-2] is the height at the top of the stack
        if h == stack[-2]:
            # if equal, just increment its length by 1,
            # no need to append the stack with the same height
            stack[-1] += 1
        elif h > stack[-2]:
            # if h is greater, append the new height to the stack
            stack.append(h)
            stack.append(1)
        else:
            # if h is lesser, purge the top of the stack of heights
            # greater than h
            back_length = 0 # back length is length meant to be added to h's length (since h is less)
                            # and also to the length of the height's being purged (since the stack is a list of increasing heights)
            while stack and h < stack[-2]:
                length = stack.pop() + back_length
                height = stack.pop() 
                max_area = max(max_area, height * length) # evaluate area before purging
                back_length = length
            
            # when the stack is processed, there are 2 scenarios to consider
            # 1. the current top height is equal to h
            # 2. the current top height is less than h
            if stack and h == stack[-2]: # scenario 1
                stack[-1] += 1 + back_length
            else: # scenario 2
                stack.append(h)
                stack.append(1 + back_length)
            
    # STEP 2: clear out the rest of the stack
    # remember that the stack is of increasing heights
    back_length = 0
    while stack:
        l = stack.pop() + back_length
        h = stack.pop()
        max_area = max(max_area, h * l)
        # if stack:
        #     stack[-1] += l
        back_length = l
    
    return max_area