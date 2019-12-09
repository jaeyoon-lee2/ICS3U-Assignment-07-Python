#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program displays 10 random number with the array


def main():
    # this function displays 10 random number with the array

    first_list = []
    second_list = []
    concatenated_list = []

    # input
    first_list_name = input("Enter the name of first list: ")
    second_list_name = input("Enter the name of second list: ")
    concatenated_list_name = input("Enter the name of concatenated list: ")
    first_things = input("Enter the things to put in {0} (Separated by "
                         "space): ".format(first_list_name))
    second_things = input("Enter the things to put in {0} (Separated by "
                          "space): ".format(second_list_name))

    print("")
    first_list = first_things.split(" ")
    second_list = second_things.split(" ")
    concatenated_list = first_list + second_list

    print("{0} are".format(concatenated_list_name))

    for counter in range(0, len(concatenated_list)):
        print("{0} ".format(concatenated_list[counter]), end="")


if __name__ == "__main__":
    main()
