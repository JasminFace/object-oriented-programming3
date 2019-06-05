def ordinal():
    number = int(input("Enter a number between 1 and 20: "))
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(str(number) + suffix)

ordinal()