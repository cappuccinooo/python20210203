names=list()
scores=list()

def highest(scores,names):
    high = 0
    temp = []
    for i in range(len(scores)):
       if scores[i] > high:
           high = scores[i]
           highname = names[i]
    temp.append(highname)
    temp.append(high)
    return temp 
def lowest(scores,names):
    low = 100
    temp = []
    for i in range(len(scores)):
        if scores[i] < low:
            low = scores[i]
            lowname = names[i]
    temp.append(lowname)
    temp.append(low)
    return temp
def average(scores):
    total = 0
    for i in range(len(scores)):
        total = total+scores[i]
    ave = total / len(scores)
    return ave



people = int(input('班上有幾個人?'))

for i in range(people):
    n = input('please input the name:')
    names.append(n)
    
    s = int(input('輸入成績'))
    scores.append(s)
print(names)
print(scores)
lo = lowest(scores,names)
print(lo[0],'拿到了最低分')
hi = highest(scores,names)
print(hi[0],'拿到了最高分')
a = average(scores)
print(a,'平均分數')









