with open("cities.txt", "r") as og_file:
    cities = og_file.readlines()
 
#Remove newline characters and sort alphabetically
 
for city in cities:
    city.strip()
    #cities = [city.strip() for city in cities]
    cities.sort()
 
#Write sorted city names to output file
 
with open("sorted_cities.txt","w") as file:
    for city in cities:
        file.write(city + "\n")
 
print("Cities sorted and writted to sorted_cities.txt")
