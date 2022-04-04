a= int(input())
num= a
cycle=0

while True:
    b= num//10
    c= num%10
    num= (c*10) + ((b+c)%10)
    cycle+=1
    if a==num:
        print(cycle)
        break