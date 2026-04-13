#!/usr/bin/env python3
"""
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
"""

from helper import Helper
import exception as e

def main():
    try:
        Helper.show_welcome_message()
        Helper.show_main_menu()
        Helper.show_sub_menu(input("Enter number here >> "))

        while Helper.do_again():
            Helper.show_main_menu()
            Helper.show_sub_menu(input("Enter number here >> "))

    except KeyboardInterrupt:
        print("\n\nQuitting program...")
    except e.InvalidOptionError as ex:
        print(f"\nError: {ex}")

    Helper.exit_message()


if __name__ == "__main__":
    main()