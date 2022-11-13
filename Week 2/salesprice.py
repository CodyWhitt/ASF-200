desc = str(input('Please enter the product description:'))
qty = int(input('How many of item {} are being purchased?'.format(desc)))
price = int(float(input('What is the regular price?')))
savings = int(float(0))

if price >= 19.99  and price < 39.99:
    savings = (price * .15)
    price = price - (price * .15)
if price >= 39.99:
    savings = (price * .25)
    price = price - (price * .25)

tax = (price * .065) * qty
preTax = price * qty
fnlPrice = preTax + tax

print('''
Your Receipt
--------------------------------------------------''')
print('{} {} @ {:,.2f} each'.format(qty,desc,price))
print('Sales Tax ${:,.2f}'.format(tax))
print('Total amount due ${:,.2f}'.format(fnlPrice))
print('You saved ${:,.2f} today.'.format(savings * qty))