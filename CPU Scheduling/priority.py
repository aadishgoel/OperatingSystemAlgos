# CPU Scheduling
### Priority Non Primitive
priority = list(map(int, input("Enter priority times: ").split()))
raw = list(map(int, input("Enter burst times: ").split()))
data = sorted(list(zip(raw, priority)), key=lambda x:x[1])
n = len(data)

c=s=0
for i in data:
    c+=i[0]
    s+=c

print('Avg. Turn Around Time',s/n)
print('Avg. Waiting Time',(s-c)/n)

"""
Enter priority times: 2 3 4 1
Enter burst times: 1 2 3 4
Avg. Turn Around Time 6.5
Avg. Waiting Time 4.0
"""
