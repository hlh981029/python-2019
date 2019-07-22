m = input()

# m[0]

# 'aaa' + 'bbb' 'aaabbb'
# 'aaa' + 123 wrong
# 'aaa' + str(123) 'aaa123'

# '123abc'
#  012345
#  -6-5-4-3-2-1

n = ['￥', '$', 'RMB', 'USD']
b = 0
c = ''

if m[0] == n[0]:
    b = float(m[1:]) / 6.78
    c = n[1]
elif m[0] == n[1]:
    b = float(m[1:]) * 6.78
    c = n[0]
elif m[0:3] == n[2]:
    b = float(m[3:]) / 6.78
    c = n[3]
elif m[0:3] == n[3]:
    c = n[2]
    b = float(m[3:]) * 6.78

print(c + str(b))
