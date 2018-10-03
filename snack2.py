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
   
 
    
    
#index = 0
#for name in names:
 #   snack = snacks[index]
  #  index = index + 1
   # print(name + " likes " + snack)k
    