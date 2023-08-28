#Write a program to calculate the amount to be paid after 8 years,where principal=5000,rate of intrest per annum =9.
P= float(input('Enter the principal:'))
R= float(input('Enter the rate of intrest per annum:'))
T=float(input(;Enter the time in years:'))
SI=(P*R*T)/100
amount=SI+P
print('Total amount:',amount)
