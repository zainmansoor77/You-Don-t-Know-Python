h = input("Enter Hours:")
r = input("enter your hourly rates :")
try:
    h = float(h)
    r = float(r)
except:
    print("enter only numeric values only")
    quit()

if h>40:
    pay = (h-40)*(1.5*r)+40*r
else:
    pay = h*r

print(pay)
