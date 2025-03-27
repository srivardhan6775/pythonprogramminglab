import random
n=random.randint(1,100)
print("guess the number")
while True:
       x=int(input("guess the number"))
       if(x<n):      
                 print("your number is low")
       elif(x>n):
                 print("your number is high")
       elif(x==n):
                 print("you won")
                 break   
   
