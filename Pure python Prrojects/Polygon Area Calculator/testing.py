def numberfromstring(string_a):
     n=list(string_a)
     for i in n:
         if i.isdigit():
             k=int(i)
             print(k)

numberfromstring("width=5")

print(str("sad2").isnumeric())