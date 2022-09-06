
def something(number):
    diff = None

    while diff != 0:
        ascending = "".join(sorted(str(number)))
        descending = "".join(sorted(str(number), reverse = True))
        next_number = int(descending) - int(ascending)
        print(descending + " - " + ascending + " = " + str(next_number))
        diff = number - next_number #Commenting this line out will give a constant number called Kaprekar's Constant and loop becomes infinite
        number = next_number

num = int(input("Enter a 4 digit number : "))
something(num)