# CPU Scheduling
### First Come First Serve Bases

data = list(map(int, input("Enter burst times: ").split()))
c=s=0
for i in data:
    c+=i
    s+=c
print('Avg. Turn Around Time',s/n)
print('Avg. Waiting Time',(s-sum(data))/n)

'''
Enter burst times: 24 3 3
Avg. Turn Around Time 27.0
Avg. Waiting Time 17.0
'''
