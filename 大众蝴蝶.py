import turtle as t


def   buffer(r,n):
##    
##    for i in range(0,n):
##        t.fd(0.0174*r)
##        t.rt(1)
##             
    t.circle(-r,n)
    return

def   fly(r , n):
    for i in range(0,2):
             buffer(r,n)
             t.rt(180-n)
    return


for  i in range(0,4):
    
    s=20
    for  j in range(0,3) :
        
        
        fly(s,90)
        s=s+10
    t.rt(90)
             
             
             
             
             
             
             
             
    
