# with open("user.txt",'a+') as r1:
#     r1.write("{'a':12}\n")
#     r1.write("{'a1':12}\n")
#     r1.write("{'a2':12}\n")
# with open("user.txt",'r') as r1:
#     li={}
#     r=r1.read()
#     print(r)
#     for a in r:
#         li.update(a)
#     print(li)
    
li={123:1233,13:113}
for k,l in li.items():
    p=li[k]
    print(p)
# print(p)