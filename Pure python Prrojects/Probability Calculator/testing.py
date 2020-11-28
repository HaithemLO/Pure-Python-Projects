import copy
import random
from random import *

class temp :
    def __init__ (self,**kwargs) :
        self.contents = []

        if(len(kwargs) ==0):
            print("at least one argument needed")
            quit()
        
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        
    
    def draw (self,amount):
        anwser = []
        leny = len(self.contents)
        while amount > 0 :
            x = uniform(0, leny)
            y = (x-(x%1))
            anwser.append(self.contents[int(y)])
            del self.contents[int(y)]
            amount -= 1
        return (anwser)

p1 = temp(red=5, orange=4, black=1, blue=0, pink=2, striped=9)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contents = []

    for k,v in expected_balls.items():
            for i in range(v):
                contents.append(k)
    
    hit = 0
    for npe in range(num_experiments):
        cat = copy.deepcopy(hat)
        drawn = cat.draw(num_balls_drawn)

        chk = False
        for e in contents:
            if e in drawn:
                chk=True
                drawn.remove(e)
            else:
                chk = False
                break

            if chk:
                hit += 1
    return hit/num_experiments
    
    


        



        

p1 = temp(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
p1.draw(5)

