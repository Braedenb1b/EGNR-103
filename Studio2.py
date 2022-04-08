#constants
totalgassold = (((97.7*31)+(99.7*28)+(104.3*31)+(103.8*30)+(101.4*31)+(110.2*30)+(110.7*31)+(112.2*30)+(106.1*31)+(112.4*30)+(98.3*30)+(105.8*31))*1000)
totaldrivers = 3100000

galperyear = (totalgassold/totaldrivers)
totalgasused = galperyear
print (galperyear)
print("Driving Oregonians used an average of", totalgasused, "gallons of gas per person in 2019")

mpg = int(input("Enter your cars average MPGe: "))
galused = 14032 / mpg

gasprice = float(input("Enter the current gas price at your current location (in $): "))
totalprice = galused * gasprice

gasprice2 = float(input("Enter the current gas price in California (in $): "))
totalprice2 = galused * gasprice2

KW_used = mpg * 33,7
KW_price = 14000/mpg/(33.7*0.18)

print("This car will use", galused, "gallons of gas per year on average or", KW_used, "Kilo Watt Hours")
print("This car will spend", totalprice, "dollars on gas per year on average if gas is $",gasprice, "at your current location")
print("This car will spend", totalprice2, "dollars on gas per year on average if gas is $",gasprice2, "in California")
print("If this car was fully electric you would spend", KW_price, "dollars on electricity")

#33.7 Kw/hr = 1 mpg
#80% at home, 20% outside
