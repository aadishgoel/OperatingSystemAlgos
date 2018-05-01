import random

class abc:
    
    def __init__(s):
        states = {0:'Thinking', 1:'Hungry', 2:'Eating'}
        s.self = [0]*5
        s.state = [0]*5

    def pickup(s,i):
        s.state[i]=1   #Hungry
        s.test(i)
        if s.state[i] != 2:
            s.wait(s.self,i)

    def putdown(s,i):
        s.state[i]=0    #Thinking
        s.test((i+4)%5)
        s.test((i+1)%5)

    def test(s,i):
        if(s.state[((i+4)%5)]!=2 and s.state[((i+1)%5)]!=2 and s.state[i]==1 ):
            s.state[i]=2
            s.signal(s.self,i)

    def wait(s,self,i):
        if not s.self[i]: s.self[i]=1

    def signal(s,self,i):
        if s.self[i]:
            s.self[i]=0
            s.pickup(i)
            


##x = abc()
##print(x.self)
##print(x.state)
##print('**********************************************************************')
##x.pickup(0)
##x.pickup(2)
##x.pickup(1)
##print(x.self)
##print(x.state)
##print('**********************************************************************')
##x.putdown(0)
##x.putdown(2)
##print(x.self)
##print(x.state)
##print('**********************************************************************')

a = abc()
for i in range(100):
    v = random.randint(0,1)
    r = random.randint(0,4)

    if not v: a.pickup(r)
    else:     a.putdown(r)
    
    print('**********************************************************************')
    print(a.self)
    print(a.state)
    
