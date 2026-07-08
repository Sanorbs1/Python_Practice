try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid integer")
else:
    print(f"Result = {y}")   # runs if no exception
finally:
    print("Done")            # always runs