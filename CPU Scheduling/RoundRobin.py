# CPU Scheduling
### shortest burst time first
tq = int(input("Enter time quantam: "))
data = list(map(int, input("Enter burst times: ").split()))
n = len(data)
t=s=0
while(max(data)>0):
    for i in range(n):
        if data[i]>0:
            t+= min(tq,data[i]-tq)
            data[i]= max(0,data[i]-tq)
            if data[i]==0:
                s+=t
        
print('Avg. Turn Around Time: ',s/n)
print('Avg. Waiting Time: ',(s-sum(data))/n)

