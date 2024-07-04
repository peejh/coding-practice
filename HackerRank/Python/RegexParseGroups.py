import re

# METHOD 1
# `search` finds first occurrence
m = re.search(r'([0-9a-zA-Z])\1', input())

# METHOD 2
# uses lazy operator *? to match as few leading characters before the repeating characters
# `match` compares pattern to entire string to make a match
m = re.match(r'.*?([^\W_])\1.*', input())

print(m.group(1) if m is not None else -1)