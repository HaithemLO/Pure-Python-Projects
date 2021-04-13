type_of_spending = ["Car","games"]
temp = [60,45]
percent = 100
temp = ""

while percent > 0 :
    temp += ("\n"+str(percent) + "|")
    percent -= 10
print(temp)
    

for i in temp :
    x = ""
    
    percent = 100
    while percent > 0 :
        if i >= percent :
            tick = "o"
        else :
            tick = ""
        x += ("\n"+str(percent)+"|  " + tick)
        percent -=10
    y = ("\n"+"o")
print(x+temp)
        
            
        
