x = {"name": "Alice",
     "age": 25
     }
y = {"city": "New York",
     "Job": "Engineer"
     }
x.update(y)
for key, value in x.items():
      print(f"{key}: {value}")