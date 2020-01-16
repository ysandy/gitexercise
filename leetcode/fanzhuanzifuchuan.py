s = 'abc'
list01 = []
# list01[:] = string[::-1]
# print(list01)
list01[:] = s
r = 0
l = len(s)-1
while r<l:
    list01[r],list01[l] = list01[l],list01[r]
    r += 1
    l -= 1
print(list01)



