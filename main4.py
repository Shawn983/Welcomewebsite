try:
    age = int(input("Enter your age:"))
    print(f"You are {age} years old !")
except ValueError:
    print("Please enter a valid integer !")
else: 
     print(f"You are {age} years old !")
finally:
    print("Thank you for using our program")