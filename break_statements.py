#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about break statements

import random


def main():
    # This function is about break statements
    answer_number = random.randint(0, 9)

    while True:
        # input
        user_string = input("Enter a number between 0 - 9: ")
        print("")

        # process
        try:
            user_number = int(user_string)
            if user_number == answer_number:
                # output
                print("You are correctly.")
                break
            elif user_number < answer_number:
                # output
                print("{} is lower.".format(user_number))
                print("")
            else:
                # output
                print("{} is higher.".format(user_number))
                print("")
        except Exception:
            # output
            print("You didn't enter an integer.")
            print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
