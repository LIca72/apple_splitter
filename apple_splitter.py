try:
    friends = int(input("How many friends do you have? "))
    portion = 10 / friends
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a number!")
else:
    print(f"Each friend gets {portion} apples!")
finally:
    print("Program finished.")
