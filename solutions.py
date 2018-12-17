

def question1(s, t):
    
    confirm = t
    
    for i in range(0 , len(s)):
        for j in range(0 , len(t)):
            if t[j] == s[i]:
                confirm.remove(t[j]) 
     
    print confirm
    
    if confirm == []:
        return True
    else:
        return False 
        
t = 'ad'
s = 'udacity'
print question1(s, t)