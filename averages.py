#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program generates random numbers using arrays and finds the average.

import random


def main():
    # this function finds the average of 10 random numbers

    num_array = []

    print("This program generates 10 random numbers and finds the average.\n")

    # process
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        num_array.append(random_num)
        print("Random number generated: {}".format(random_num))

    average = sum(num_array) / 10

    # output
    print("\nThe average is {0:.2f}.".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
