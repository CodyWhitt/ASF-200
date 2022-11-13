applePrice = float(.50)
name = str(input("Please enter your name: "))
amt= int(input('Hi {}, Apples cost ${:.2f} each. How many would you like to buy?'.format(name,applePrice)))
print('Thanks {} for your purchase of {} apples at a cost of ${:.2f} each'.format(name, amt, applePrice))