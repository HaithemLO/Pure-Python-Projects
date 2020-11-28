class Category:
    def __init__(self,Item):
        self.Item = Item
        self.ledger = []
        self.amount_left = 0


    def deposit(self,amount,description="desposit"):
        self.amount_left +=amount
        self.ledger.append(str(amount)+" "+description)
        
        
    
    def withdraw(self,amount,description=""):
        if amount > self.amount_left :
            print(False) 
        else:
            self.ledger.append(str(-amount)+" "+description)
            self.amount_left -= amount
            print(self.ledger)
            print(True) 
    
    def get_balance(self):
        return self.amount_left
    
    def transfer(self,amount,Item):
        if amount > self.amount_left :
            print(False)
        else :
            self.ledger.append(str(-amount)+" Transfer-to-"+str(Item.Item))
            self.amount_left -= amount
            Item.deposit(amount)
            # print(self.amount_left)
            # print(self.ledger)
    
    def check_funds(self,amount):
        if amount > self.amount_left :
            print(False)
        else :
            print(True)
    
    def budget (self,Item):
        leny = round((30-len(self.Item))/2)
        print(leny*"*"+self.Item+leny*"*")
        for i in self.ledger :
            print("%-18s %-5s" %(str(i.split()[1]),str(i.split()[0]).rjust(12)))
        print("amount left: ",self.amount_left)

    def get_ledger (self):
         return self.ledger


food = Category("Food")

food.deposit(100)

# food.withdraw(2132,"gay-food")



cloths = Category("cloths")

food.transfer(50,cloths)

x = str(food.get_ledger()[0]).split()[0]

cloths.withdraw(40,"gay-foods")



# cloths.budget(cloths)

# food.get_balance()

# cloths.get_balance()

# food.transfer(2000,cloths)
# cloths.get_balance()




def create_spend_chart(Category):
    PercentList = []
    NameList = []
    
    for i in Category:
        x = ((int(str(i.get_ledger()[0]).split()[0])-int(str(i.get_balance())))/int(str(i.get_ledger()[0]).split()[0]))*100
        y=(x-(x%10))
        PercentList.append(y)
        NameList.append(i.Item)
        print(PercentList)
        print(NameList)
    print('Percentage spent by category')
    for i in PercentList :
        percent = 100
        
    
        while percent > 0 :
            if i >= percent :
                tick = "o"
            else :
                tick = ""
            print(str(percent)+"|  " + tick  )
            percent -=10

        
       
        
        
        
        
    
       

create_spend_chart([food,cloths])




    
    
