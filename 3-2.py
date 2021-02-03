a=[]
total = 0
high = 0
low = 100
n = int(input('班上有幾個人?'))

for i in range(n):
    score = int(input('輸入成績'))
    total = total+score
    if high < score:
        high = score
    if low > score:
        low = score
    a.append(score)
    
average = total / n
print(a)
print('average:',average)
print('high:', high)
print('low', low)
    