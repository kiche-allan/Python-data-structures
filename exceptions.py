#program to get users name from the terminal
# use try and accept construct to handle errors

try:
    Age= int(input('Age: '))
    income = 2899
    risk = income / Age
    print(Age)

except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Value')

