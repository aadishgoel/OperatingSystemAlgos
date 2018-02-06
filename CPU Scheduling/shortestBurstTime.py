# CPU Scheduling
### shortest burst time first

data = sorted(list(map(int, input("Enter burst times: ").split())))
n = len(data)
c=s=0
for i in data:
    c+=i
    s+=c

print('Avg. Turn Around Time',s/n)
print('Avg. Waiting Time',(s-sum(data))/n)

"""
Enter burst times: 4 2 3 1 7
Avg. Turn Around Time 7.4
Avg. Waiting Time 4.0
"""
