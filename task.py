"""
Update the get_fizzbuzz_list function. The function has to generate and return a list with numbers from 1 to n inclusive where the n is passed as a parameter to the function. But if the number is divided by 3 the function puts a Fizz word into the list, and if the number is divided by 5 the function puts a Buzz word into the list. If the number is divided by both 3 and 5 the function puts FizzBuzz into the list.
"""

from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    my_list = []

    for i in range(1,n+1):
        if  i%3==0 and i%5==0:
            my_list.append("FizzBuzz")
        elif  i%3==0:
            my_list.append("Fizz")
        elif  i%5==0:
            my_list.append("Buzz")
        else:
            my_list.append(i)

    return my_list

