number = input("Please enter a positive number: ")

while number.isdigit() == False:
    number = input("Invalid Input. Please enter a positive number: ")

r = range(0,int(number)+1, 2)

for n in r:
    print(n)