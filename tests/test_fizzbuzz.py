import sys
import os

# Add parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fizzbuzz import fizzbuz

def test_fizzbuz():
    assert fizzbuz(3) == 'Fizz'
    assert fizzbuz(5) == 'Buzz'
    assert fizzbuz(15) == 'FizzBuzz'
    assert fizzbuz(7) == 7 