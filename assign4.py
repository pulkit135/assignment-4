#Question 1
marks=int(input("Enter number of marks:"))
if (marks>=80):
    print('Grade A')
elif(marks>=60 and marks<80):
    print('Grade B')
elif(marks>=50 and marks<60):
    print('Grade C')
elif(marks>=45 and marks<50):
    print('Grade D')
elif(marks>=25 and marks<45):
    print('Grade E')
else:
    print('Grade F')         

#Question 2
year = int(input("Which year do you want to check? "))
if(year%4==0):
    if(year%100!=0):
        print("Leap year.")
    elif(year%100==0):
        if(year%400==0):
            print("Leap year.")
        else:
            print("Not leap year.")
else:
    print("Not leap year")                   

#Question 3
import random
print("Find the product of the following 2 numbers:")
for i in range (1,11):
  num1=random.randint(0,11) #Generating 2 random numbers
  num2=random.randint(0,11)
  
  print(num1)
  print(num2)

  answer=int(input("Enter your answer"))
  prod=num1*num2       #Calclating actual product
  print('Question',i,':',num1,'x',num2,'=',answer)
  if(answer==prod):    
      print('Right!')
  else:
      print('Wrong. The correct answer is',prod) 

#Question 4

for candy in range (200):
    if candy%5 !=2:
        continue    #use of continue so that it checks all the conditions
    if candy%6!=3:
        continue
    if candy%7!=2:
        continue
    print(str(candy)+'candies are in the bowl')    
    break  
