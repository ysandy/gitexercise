list01 = [1,2,3,4,5,6,7] #len(list) = 7,  i(0-6)
# list01 = [1,2]
k = 3
#2,1

# k = 2  # [5,6,7,1,2,3,4]
# # 后面依次取k 个数放前面，len(list)-k 个数依次放后面
# # n = list01[len(list01) - k:len(list01)]list01[len(list01)-k-i]
# # print(n)

#不能通过全部用例，？
# c = k%len(list01)
# for i in range(c):
#     tmp = list01[len(list01)-c+i]
#     list01.remove(list01[len(list01)-c+i])
#     list01.insert(i,tmp)
# print(list01)


# for i in range(k%len(list01)):
#     list01.insert(0,list01.pop())
# print(list01)

# c = k%len(list01)
# list01[:] = list01[-c:]+list01[:-c]
# print(list01)

# old_list = list01[:]
# for i in range(len(list01)):
#     list01[(i+k)%len(list01)] = old_list[i]
# print(list01)

#三次反转

n = len(list01)

k %= n

list01[:k+1] = list01[:k+1][::-1]
list01[k+1:] = list01[k+1:][::-1]
list01[:] = list01[::-1]
print(list01)






