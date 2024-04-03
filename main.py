def mileKilo(x):
    convertRate = 1.60934
    return x * convertRate


def kiloMile(x):
    convertRate = 0.62137
    return convertRate * x


q1 = input("Do you want to type in the distance in miles or kilometers? (k/m) ")
if q1 == "m" or q1 == "M":
    q2 = float(input("How many miles would you like to scooter?"))
    print("That is", mileKilo(q2), "kilometers")

    time = q2 / 15
    print(time * 60)

    a = 1 + 0.15 * time
    if time <= 5:
        b = 2.5 * time
    else:
        b - 2.5 * 5 + 0.12 * time
    c = 5 + 0.06 * time

    if a < b and a < c:
        print("use company A.", "it will cost", a)
    elif b < a and b < c:
        print("use company B.", "it will cost", b)
    else:
        print("use company C.", "it will cost", c)


elif q1 == "k" or q1 == "K":
    q2 = float(input("How many miles would you like to scooter?"))
    print("That is", kiloMile(q2), "kilometers")
    print((time(q2, 15)) * 60)
