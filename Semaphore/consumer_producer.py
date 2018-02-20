## Producer Consumer Problem

N = 10 # Bounded limit 
s=1 # Binary Semaphore
e=N # Counting Semaphore ## Empty blocks
f=0 # Counting Semaphore ## Full Blocks

def signal(x):
    x+=1
    return x

def wait(x):
    while x<=0: pass
    x-=1
    return x

def consumer():
    global e,s,f
    f,s = wait(f),wait(s)
    print("Consumed")
    s,e =signal(s),signal(e)


def producer():
    global e,s,f
    e,s=wait(e),wait(s)
    print("Produced")
    s,f = signal(s),signal(f)

while True:
    print("\t\t\t\tProduced item till now:",f)
    choice = int(input('''Press 1: For Consumer\nPress 2: For Producer\n'''))
    if choice==1:
        if f<1: print('No item to be consumed')
        else: consumer()
    elif choice==2:
        if e<1: print('No more space to produce') 
        else: producer()
    else:
        print('Invalid Choice')



''' ****OUTPUT****
				Produced item till now: 0
Press 1: For Consumer
Press 2: For Producer
1
No item to be consumed
				Produced item till now: 0
Press 1: For Consumer
Press 2: For Producer
2
Produced
				Produced item till now: 1
Press 1: For Consumer
Press 2: For Producer
1
Consumed
'''





























































        
