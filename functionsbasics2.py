# def countdown(num):
#     newlist=[]
#     for i in range(num,-1,-1):
#         newlist.append(i)
#     return newlist
# print(countdown(5))

# def printreturn(list):
#     print(list[0])
#     return list[1]
# printreturn([1,2])

# def pluslen(list):
#     return list[0]+len(list)
# print(pluslen([1,2,3,4,5]))

# def second(list):
#     newlist=[]
#     count=0

#     for i in list:
#         if len(list)<2:
#             return "False"
#         if i>list[1]:
#             count+=1
#             newlist.append(i)
#     print(count)
#     return newlist
# print(second([3]))

# def thisthat(length,value):
#     newlist=[]
#     for i in range(0,length,1):
#         newlist.append(value)
#     return newlist
# print(thisthat(5,2))