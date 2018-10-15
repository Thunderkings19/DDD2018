names = {
        "Michael" : "",
        "Diana" : "",
        "Robyn" : ""
        }
  
for name in names:
    length = len(name) 
    snack = input(f"Hello {name}, what is your favorite snack?")
    names[name] = snack
    print(f"{name} has {length} characters and your favourite snack is {snack}")


for name, snack in names.items():
        print(f"{name} likes {snack}")

