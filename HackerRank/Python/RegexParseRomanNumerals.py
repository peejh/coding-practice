# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

regex_pattern = r"^(M{0,3})(C(D|M|C{0,2})|DC{0,3})?(X(L|C|X{0,2})|LX{0,3})?(I(V|X|I{0,2})|VI{0,3})?$"
regex_pattern2 = r"^(M{0,3})(CD|CM|D?C{0,3})(XL|XC|L?X{0,3})(IV|IX|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))