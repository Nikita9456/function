
def number(limit):
    i=1
    sum=0
    while i<=num1:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum)
num1=int(input("enter the num"))
number(num1)
