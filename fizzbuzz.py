def fizzBuzz(n):
    for i in range(n):
        i += 1
        fizz = (i / 3)
        buzz = i / 5
        fizzbuzz = (i / 15)

        if fizzbuzz - int(fizzbuzz) == 0:
            print("fizzbuzz")
        elif fizz - int(fizz) == 0:
            print("fizz")
        elif buzz - int(buzz) == 0:
            print("buzz")
        else:
            print(i)


fizzBuzz(100)

def fizzBuzz2(n):
    for i in range(n):
        output = ""
        i += 1
        fizz = (i / 3)
        buzz = i / 5
        fizzbuzz = (i / 15)

        if fizzbuzz - int(fizzbuzz) == 0:
            print("fizzbuzz")
        elif fizz - int(fizz) == 0:
            print("fizz")
        elif buzz - int(buzz) == 0:
            print("buzz")
        else: