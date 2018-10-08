import json

with open("movies.json") as f:
    movies = json.load(f)

question = input("From which year do you want to see the movies?")
question = int(question)

with open("movies.json") as f:
    movies = json.load(f)
    
for movie in movies:
    year = movie["year"]
    if year == question:
        print(f"{movie['title']}")


