#Ask user to input the names of the pupils in a class and enter stop when finished
#Count and print out the total of the names inputted by user

count_names = 0

while True:
   names = input("Please enter the name of a pupil in the class, enter 'Stop' once finished: ").lower()
   if names != "stop":
    count_names += 1 
   else: 
       break

print(count_names)

    

    