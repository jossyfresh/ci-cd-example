def fizzbuz(x):
    if x % 5 and x % 3:
        return 'FizzBuzz'
    elif x % 3:
        return 'Fizz'
    elif x % 5:
        return 'Bu'
    else:
        return x