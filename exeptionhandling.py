try:
    num = int(input("Enter a number: "))
    print(f"Half of your number is {num/2}")
except ValueError:
    print("Oops! Please enter a valid number.")
except ZeroDivisionError:
    print("no division by zero")
else:
    print("you entered the correcr value number")
finally:
    print("Thank you for using the program")

def division():
  try:
    num = int(input("Enter a number: "))
    return 10 / num
  except ValueError:
    print("That's not a number!")
  except ZeroDivisionError:
    print("Cannot divide by zero!")
print(division())

try:
   num=int(input("enter a number:"))
   result=100/num
   print(f"result is: {result:.2f}")
except ZeroDivisionError:
   print("Oops! No division by zero allowed")
except ValueError:
   print("Oops! Please enter a valid number.")
finally:
   print("Thanks for using the program")

   


