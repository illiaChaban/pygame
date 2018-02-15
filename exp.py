from random import randint

def get_random(start, end):
    return randint(start, end)

def my_function(lst):
    new_lst = [0 for i in lst]
            
    random_lst = []
    
    while len(random_lst) != len(lst):
        x = get_random(0, len(lst)-1)
        if not x in random_lst:
            random_lst.append(x)
         
    for j in range(0, len(lst)):
        new_lst[random_lst[j]] = lst[j]
        
    return new_lst
        
        
        
    
    
        
        
        
print my_function('test input')
