name=input("請輸入你的名字")
hourly_salary=int(input("請輸入你的年薪"))
annual_salary=hourly_salary*8*300
monthly_fee=int(input("請輸入你的年支出"))
annual_fee=monthly_fee*12
annual_savings=annual_salary-annual_fee
print("%s每年存萬金額%d元"%(name,annual_savings))                 
print("沈均叡每年存款%d元"%annual_savings)
