def fibonacci(n):
    a = 0
    b =1
    for i in range(n):
        print(a)
        a,b = b,a+b
fibonacci(7)

#Sort a list without using sort()
def sorting(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] > num[j]:
                num[i],num[j]=num[j],num[i]
    return num
print(sorting([1,3,2,6,5,4,8,9,7,10]))