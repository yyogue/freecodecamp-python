try:
    num = int(input("Enter a number"))
    result = num / 10
    print(f"Results: {result}")
except ZeroDivisionError:
    print("Cannot divie by zero")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution completed.")