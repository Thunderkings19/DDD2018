#Two variables for two different name inputs
first = input("What is the first name").strip().lower()
second = input("What is the second name").strip().lower()

#Making sure the names are not the same
if first == second: 
    print("You entered the same name!")
else:
    print("You entered " + first + " and " + second)

#Calculating the difference in charachters of the names
difference = len(first) - len(second)

#Giving the difference a positive number
positive_difference = abs(difference)

#Giving the difference a percentage outcome
if positive_difference == 0:
    print("You are a 100% match made in heaven!")

elif positive_difference == 1:
    print("You are a 90% match, you will be a good couple!")

elif positive_difference == 2:
    print ("You are a 80% match, you will be a good couple!")

elif positive_difference == 3:
    print ("You are a 70% match, you will be a good couple!")

elif positive_difference == 4:
    print ("You are a 60% match, you will manage a relationship by working hard!")

elif positive_difference == 5:
    print ("You are a 50% match, you will manage a relationship by working hard!")

elif positive_difference == 6:
    print ("You are a 40% match, you will manage a relationship by working hard!")

elif positive_difference == 7:
    print ("You are a 30% match, you will manage a relationship by working hard!")

elif positive_difference == 8:
    print ("You are a 20% match, you will probably won't make it until the end..")

elif positive_difference == 9:
    print ("You are a 10% match, maybe find someone else?")

else:
    print("You are no match at all")


