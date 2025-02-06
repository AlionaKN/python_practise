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

