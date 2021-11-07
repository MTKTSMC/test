def computepay(h, r):

 
    if h > 40 :
        p=(40*r)+((h-40)*1.5*r)

    else :
        p=h*r
    
    return p


hrs = input("Enter Hours:")
rate = input("Pay rate:")
h=float(hrs)
r=float(rate)

p = computepay(h, r)
pay=p
print("Pay", pay)