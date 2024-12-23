number = int(input("Enter a number to see its multiplication table: "))

i = 1

while i <= 10:
    print(str(number) + "*" + str(i) + "=" + str(number*i))
    i=i+1
