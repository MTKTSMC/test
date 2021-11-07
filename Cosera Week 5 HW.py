hrs = input("Enter Hours:")
rat = input("Pay rate ")
lit = input("limit")

pay=float(pay)

h = float(hrs)
r = float(rat)
lit = float(lit)
44
if h >=lit :
	pay=((h-lit)*1.5*r)+lit*r


print(pay)