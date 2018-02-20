## Reader Writer Problem
wrt=1   # Binary Semaphore
mutex=1 # Binary Semaphor
count=0 

def signal(x):
    x+=1
    return x

def wait(x):
    while x<=0: pass
    x-=1
    return x

def writer():
    global wrt
    wrt = wait(wrt)
    print("Write")
    wrt =signal(wrt)


def reader():
    global wrt,count,mutex
    mutex = wait(mutex)
    count=signal(count)
    if count==1: wrt=wait(wrt)
    mutex = signal(mutex)
    print('Read')
    mutex = wait(mutex)
    count = wait(count)
    if not count: wrt=signal(wrt)
    mutex = signal(mutex)
    print(count)
    

while True:
    print("\t\t\t\tReaders till now:",count)
    choice = int(input('''Press 1: For Writer\nPress 2: For Reader\n'''))
    if choice==1:
        writer()
    elif choice==2:
        reader()
    else:
        print('Invalid Choice')






























































        
