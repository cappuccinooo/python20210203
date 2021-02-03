a=[]
name=[]
total = 0
high = 0
low = 100
n = int(input('班上有幾個人?'))

for i in range(n):
    stuname = input('please input the name:')
    score = int(input('輸入成績'))
    total = total+score
    name.append(stuname)
    a.append(score)

for i in range(n):
    if a[i] > high:
        high = a[i]
        highname = name[i]

for i in range(n):
    if a[i] < low:
        low = a[i]
        lowname = name[i]
    
average = total / n
print(a)
print('average:',average)
print('high:', high,highname)
print('low', low,lowname)