n=int(input("Enter a positive number: "))
sum=0
count=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
        count+=1
print("Sum of even numbers from 1 to",n,"is:",sum)
print("Count of even numbers from 1 to",n,"is:",count)