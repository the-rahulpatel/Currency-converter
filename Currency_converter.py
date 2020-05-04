from forex_python.converter import CurrencyRates, CurrencyCodes

from forex_python.bitcoin import BtcConverter

c = CurrencyRates()

curr = CurrencyCodes()

bt = BtcConverter()



def money():

	first_q = input("Type 'c' if you wish to know the rate of currency, 't' for converting currency or 's' for alternate information: ")
	
	if first_q == 'c':
		c1 = input("Enter country name one: ").upper()
		c2 = input("Enter country name two: ").upper()
		print(c.get_rate(c1, c2))

	elif first_q == 't':
		t1 = input("Enter country name one: ").upper()
		t2 = input("Enter country name two: ").upper()
		t3 = int(input("Enter the amount of currency: "))

		print(c.convert(t1, t2, t3))

	else:
		s1 = input("Type sym for symbols or name for currency name: ")
		if s1 == 'sym':
			s2 = input("Enter the name of the country: ").upper()
			print(curr.get_symbol(s2))
		else:
			s3 = input("Enter the country: ").upper()
			print(curr.get_currency_name(s3))

def bitcoin():
	bt1 = input("Enter the country name: ").upper()
	print(bt.get_latest_price(bt1))


over_view = input("'m' or 'c': ")

if over_view == 'm':
	money()
else:
	bitcoin()

