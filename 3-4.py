a=[]
total = 0
high = 0
low = 100
n = int(input('班上有幾個人?'))

for i in range(n):
    name = input('輸入名子')
    score = int(input('輸入成績'))
    total = total+score
    a.append(name)
    a.append(score)

for i in range(1,n*2,2):
    if a[i] > high:
        high = a[i]
        highname = a[i-1]

for i in range(1,n*2,2):
    if a[i] < low:
        low = a[i]
        lowname = a[i-1]
    
average = total / n
print('average:',average)
print('high:', high,highname)
print('low', low,lowname)

    
    