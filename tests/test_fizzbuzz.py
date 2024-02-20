from fizzbuzz import fizzbuz

def test_fizzbuz():
    assert fizzbuz(3) == 'Fizz'
    assert fizzbuz(5) == 'Buzz'
    assert fizzbuz(15) == 'FizzBuzz'
    assert fizzbuz(7) == 7 