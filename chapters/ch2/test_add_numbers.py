from chapters.ch2.add_numbers import add, is_even, convert_to_number


def test_convert_string_to_number():
    number = convert_to_number('5')
    assert number == 5


def test_4_is_even():
    assert is_even(4)

def test_5_is_odd():
    assert is_even(5) is False

def test_string_input():
    output = add('carl', 2)
    assert output == 'error: invalid numbers entered'


def test_add_odd_even_num():
    odd_even_sum = add(2, 3)
    assert odd_even_sum == 5
    assert is_even(odd_even_sum) is False

# Scenario: Adding one odd and one even number returns an odd number
# Given x=2 and y=3
# When added together
# Then the sum should be 5 and odd


def test_add_negative_num():
    negative_num = add(-2, -3)
    assert negative_num == -5


#Scenario: Adding two negative numbers returns a negative number
#Given x=-2 and y=-3
#When added together
#Then the sum should be 5 and negative