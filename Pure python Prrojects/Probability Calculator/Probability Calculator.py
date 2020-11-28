# import copy
# import random
# import re

# class Hat:
#     def __init__ (self,**kwargs):
#         contents = []
#         self.temp = temp

#         def remove_char(arg1) :
#             arg1 = list(arg1)
#             arg1.remove("=")
#             return ''.join(arg1)
        
#         for i in temp :
#             x = str(remove_char(i))
#             temp = re.compile("([a-zA-Z]+)([0-9]+)") 
#             res = temp.match(x).groups() 
#             contents.append(res)
#         print(contents)
   
# p1 = Hat((blue=9,red=999))

# a = ['red', 'red', 'red', 'red', 'red', 'orange', 'orange']
# b= ['red', 'red']

# n = len(b)
# res = any(b == a[i:i + n] for i in range(len(a) - n + 1))

# print(res)

kwargs = {"red":2,"green":1}

contents = []
for k,v in kwargs.items():
            for i in range(v):
                contents.append(k)
print(contents)



