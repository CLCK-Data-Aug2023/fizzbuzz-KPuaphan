# add your code here

for n in range(1,101):
    if n % 5 == 0 and n % 3 ==0:
        print("fizzbuzz")

    elif n % 3 == 0:
        print("fizz")

    elif n % 5 == 0:
        print("buzz")

    else:
        print(n)