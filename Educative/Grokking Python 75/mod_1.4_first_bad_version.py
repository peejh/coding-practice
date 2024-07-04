# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/6486450535268352

# -- DO NOT CHANGE THIS SECTION -----------------
    
# import main as api_call

# def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
#     return api_call.is_bad(v)

def is_bad_version(s):
    return False
# ----------------------------------------------- 

def first_bad_version(n):
    first, last = 1, n
    api_count = 0

    while first <= last:
        mid = (first + last) // 2
        api_count += 1 # this is bad technically because the api call has not been made yet
        if is_bad_version(mid):
            # in official solution, this is not needed because loop will terminate when
            # last < first, leaving first with the correct value of the first occurrence
            # of bad versions
            if first == mid:
                return [mid, api_count]
            last = mid - 1
        else:
            first = mid + 1
        
    return [first, api_count]