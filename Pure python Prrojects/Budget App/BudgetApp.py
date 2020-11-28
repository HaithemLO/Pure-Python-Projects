type_of_spending = ["Car","games"]
temp = [60,45]
percent = 100
gay = ""

while percent > 0 :
    gay += ("\n"+str(percent) + "|")
    percent -= 10
print(gay)
    

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
print(x+gay)
        
            
        
