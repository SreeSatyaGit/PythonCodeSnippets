from collections import Counter
val = list('ccaaab')
vals = set(val)
countVals = {}
for alpha in vals:
    count = val.count(alpha)
    countVals[alpha] = count
char_list = [k * v for k, v in countVals.items()]
ans = ''.join(char_list)
char_count = Counter(ans)

sorted_string = ''.join(sorted(ans, key=lambda x: char_count[x]))
print(sorted_string)