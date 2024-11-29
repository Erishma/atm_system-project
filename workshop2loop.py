#break and continue statement

for num in range(10):
    print(num)
    if num == 5:
        break

#function - Block of Executable code
 #stores values and can be used to time and again by calling function


num1 = 12
num2 = 34
print(num1 + num2)

def add(num1,num2): #function definition
    print(num1 + num2)
#function call

add(12,34)
add(34,67)

def addition(*nums): # nums = {12,23,34,56,67,68,79,89}
    print(nums)
addition(12,23,34,45,56,67,68,79,89)
#ATM System 
balance = 10000
pin = 2314

print("**Insert your card please**")
pin_num = int(input ("Enter your pin please:\n"))
if pin_num == pin:
    while True:
        print('''
             1 - check balance
             2 - deposit
             3 - withdraw
             4 - exit
''')
    print("further processing...")
else:
    print("PIN Number is wrong !!, Try Again ")