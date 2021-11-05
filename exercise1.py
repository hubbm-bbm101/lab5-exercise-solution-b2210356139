number = int(input("Enter a number"))
evensum = 0
evencount = 0
oddsum = 0

for i in range(number+1):
    if i % 2 == 0:
        evensum = evensum + i
        evencount = evencount + 1
    else:
        oddsum = oddsum + i

average = evensum / evencount

print("Sum of odd numbers is {}".format(oddsum))
print("Average of even numbers is {}".format(average))