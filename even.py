#Ask user to enter a number 
#Using a while loop, print all even numbers starting from 1 up to the number given by user  

number = int(input("Please enter a number: "))
i = 1

while i <= number:
    if i % 2 == 0:
        print(i)
    i += 1
