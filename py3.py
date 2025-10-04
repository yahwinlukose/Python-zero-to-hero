principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("enter the principle amount: "))
    if(principle<=0):
        print("Principle amount should be greater than zero")
while rate<=0:
    rate=float(input("enter the rate: "))
    if(rate<=0):
        print("rate should be greater than zero")
while time<=0:
    time=float(input("enter the time in years: "))
    if(time<=0):
        print("Principle amount should be greater than zero")
total_amount=principle*(1+rate*time/100)
print(f"The total amount after {time} years is: {total_amount}")                        