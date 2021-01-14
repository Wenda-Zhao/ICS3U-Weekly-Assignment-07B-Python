#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for list


import random


def sum_of_numbers(my_numbers):
    # this functions add up all the numbers in the list

    total = 0

    for loop_number in my_numbers:
        total += loop_number

    return total


def main():
    # this function uses a list

    my_numbers = []

    # input
    print("The numbers are ")
    for loop_counter in range(0, 9):
        random_number = random.randint(0, 10)
        my_numbers.append(random_number)
        print("{0}, ".format(random_number), end="")
    print("")

    sum_number = sum_of_numbers(my_numbers)

    print("The sum of all the numbers is: {0} ".format(sum_number))


if __name__ == "__main__":
    main()
