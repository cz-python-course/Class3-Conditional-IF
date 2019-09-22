name = input('What is your name')
dayOne = input('How many cups of coffee you drank 1 day ago?')
dayTwo = input('How many cups of coffee you drank 2 days ago?')
dayThree = input('How many cups of coffee you drank 3 days ago?')
average = (int(dayOne) + int(dayTwo) + int(dayThree)) / 3

# Solution
if average < 5:
    print('Drink More')
elif average == 5:
    print('Good')
else:
    print("You drank too much")