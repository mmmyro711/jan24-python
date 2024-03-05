# Create a data structure that will fit the following:

# Kumo has a salary of 15000 and is 23 years old.
# He owns a few items such as a car, laptop, tv, and monitor. 
# Mike is another person who makes 10000 and is 20 years old. 
# He owns a car, PC, smartwatch, and boat

persons =[ {
    
        "name": "Kumo",
        "age" : "23",
        "salary": "15000$",
        "items": ["car", "laptop", "tv", "monitor"]
    },

{
        "name": "Mike",
        "age" : "20",
        "salary": "10000",
        "items" : ["car", "PC", "smartwatch", "boat"]
}
]
for person in persons:
    print("-------------------------------------------")
    for info in person.items():
        print(info)

