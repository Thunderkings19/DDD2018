movie = {
 "title" : "Star Wars: The last jedi",
 "year" : 2017,
 "duration" : 120,
 "director" : "Joop"
 }

movie["actors"] = ["Harrison Ford", "Rutger Hauer", "Sean Young"]

for key in movie:
    val = movie[key]
    if key == "duration":
        val = f"{val} minutes"
    if key == "actors":
        val = ", ".join(val)
    print(f"{key}: {val}")
    



    