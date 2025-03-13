def biggest_number(a,b,):
 if a>b:
    print(" A is bigger")
 else:
    print("b is bigger")
biggest_number(12,14)

def check_os(opsystem):
    if(opsystem== "windows"):
        print("switc  to linux")
    elif opsystem== "linux" or opsystem=="macos":
        print("you ar godd to go")

for i in range(1,5):
    check_os("linux")

def num_range():
    for i in range(1,11):
       print (i)

num_range()

# def sum_natural_numbers(n):
#   sum_n = n*(n+1)/2 
# print(f"The sum of the first {n} natural numbers is: {sum_n}")

# n = int(input("Enter a number: "))
# sum_of_natural_numbers(n) 
