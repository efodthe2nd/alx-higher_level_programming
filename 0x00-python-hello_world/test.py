age = input("how old are you? ")
age = int(age)
if age >= 1 and age <= 5:
    print("Go to Kindergarted")
elif age > 5 and age <= 17:
    print(f"go to grade {age - 5}")
elif age > 17:
    print("Go to college")
else:
    print("no age given")
