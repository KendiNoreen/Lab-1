#Open a new Window and Write, Save, and Run the following program that reads a number and writes its square:

import math
def main():
    num = int(input("Enter a Number: "))
    result= num**2
    print("The square of", num, "is: ", result)
main()

def main():
    num = int(input("Enter a Number: "))
    result= math.sqrt(num)
    print("The squareroot of", num, "is: ", result)
main()


#This factorial computes the factorial of the number entered by the user.

def factor():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(1,n+1):
        fact=fact*factor
    print("The factorial of",n, "is", fact)

factor()

#This factorial computes the factorial of the number entered by the user.


def factor():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(1,n+1):
        fact=fact*5
    print("The factorial of",n, "is", fact)

factor()

# This program finds the sum of numbers from 1 to 1000 using a for loop.

n = int(input("Enter number to caluculate sum: "))
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
print("Sum of first ", n, "number is: ", sum)

#This program inputs 5 numbers from the user in a loop and finds the sum of the numbers.
def main():
    n = int(input("Enter number: "))
    sum = 0
    # loop from 1 to n
    for num in range(1, n + 1):
        sum = sum + num
    print("Sum of first", n, "numbers is: ", sum)

main()

#this program modifys the above program so that it finds the sum and also the average of the 5 numbers.

def main():
    n = int(input("Enter number: "))
    sum = 0
    # loop from 1 to n
    for num in range(1, n + 1):
        sum = sum + num
        average = sum / n
    print("Average of", n, "numbers is: ", average)

main()






