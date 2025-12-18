# #  1.  shop bill calculator

# item1 = float(input("item1: "))
# item2 = float(input("item2: "))
# item3 = float(input("item3: "))

# totalAmount = item1+item2+item3

# if totalAmount >1000:
#     discount = 0.05*totalAmount
    
# else:
#     discount = 0
    
# print("Total Amount: ",totalAmount)
# print("Discount: ",discount)
# print("Final payable amount: ",totalAmount-discount)

# # # ====================================================================================

# # 2.  Mobile recharge

# rechargeAmt = int(input("Recharge Amount: "))
# talktime = 0
# if rechargeAmt >= 199:
#     talktime = rechargeAmt*0.01
    
# # FnlBalance = rechargeAmt + talktime
# print("Final Balance is: ", rechargeAmt+talktime)

# # # ====================================================================================

# # 3.  Electricity bill

# unit = float(input("Enter Unit: "))
# payable_bill = 0

# if unit <=100:
#     payable_bill = unit*3
    
# elif unit<=200:
#     Abunit = 100 - unit
#     payable_bill = (100*3)+(Abunit*5)
    
# else:
#     payable_bill = (100*3) + (100*5) + ((unit-200)*7)
    
# print("Final Payable Bill: ",payable_bill)

# # # ====================================================================================

# # 4.  Print the Patern


n=int(input("Enter the number: "))

count = 0
for i in range(1,n+1):
    count = count + i
    
b = count

for i in range (1,n+1):
    n = b
    for i in range(1,i+1):
        print(n," ", end=" ")
        n+=1
        
    print()
    b = b-i-1
