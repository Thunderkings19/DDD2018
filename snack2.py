friends = [
    ["Michael"],
    ["Diana"],
    ["Robyn"]
]


for person in friends:
    length = len(person[0])
    print(str(person[0]) + " is " + str(length) + " characters")       
    snack = input("Hello " + str(person[0]) + ", what is your favorite snack?")
    person.append(snack)
    
for person in friends:
    print(person[0] + " likes " + person[1])
   
 
    
    

    
