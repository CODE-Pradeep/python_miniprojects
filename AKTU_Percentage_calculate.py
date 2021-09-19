
#enter all of your b.tech semester marks

a = int(input("enter your 1st year marks: "))
b = int(input("enter your 2nd year marks: "))
c = int(input("enter your 3rd year marks: "))
d = int(input("enter your 4th year marks: "))

#the rule of calulating of B.tech marks is 25% of 1st year
#50% of 2nd year and 75% of 3rd year and 100% of the 4th year marks will be counted  

first =a*25/100
sec =b*50/100
third =c*75/100
fourth =d*100/100

sum=first+sec+third+fourth
result=sum/4950*100

# the value 4950 is sum of total value from 
#25%of 1800=450
#50% of 2000=1000 same as 
#75% of 2000=1500
#100% of 2000=2000
#sum of 450+1000+1500+2000=4950

print("your b tech presnetage is :",result)
