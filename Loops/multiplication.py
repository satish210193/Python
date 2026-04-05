
# ##Multiplication table of a number using while loop
# n = 1
# no = int(input("Enter a number to get the table: "))
# print(f"multipcation of a {no}")
# while n<=10:
#     print(f"{no} * {n} = {no*n}")
#     n += 1
    
    

## Using for loop
no = int(input("Enter a number to get the table: "))
print(f"multipcation of a {no}")
for i in range(1, 11):
    print(f"{no} * {i} = {no * i}")

