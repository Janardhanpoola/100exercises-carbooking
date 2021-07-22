def giveBackLightChange(x,y):
    change = y-x
    if (y-x)<0:
        return "change cant be -ve"
    tens = fives = ones =0
    if(change/10) >= 1:
        tens = int(change/10)
        change = change % 10
        
    if (change/5 >= 1):
        fives = int(change/5)
        change = change % 5
        
    if (change/1 >= 1):
        ones = int(change/1)
        
    return f'tens:{tens} , fives:{fives}, ones:{ones}'
    
print(giveBackLightChange(489,50))