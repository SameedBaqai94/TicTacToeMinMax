#!/usr/bin/python3
# -*- coding: utf-8 -*-
import game as gm

def main():
    print("Welcome To Tic Tac Toe")
    print("You can 1v1 with others or")
    print("compete with an AI")
    print("")
    choice = input("1 for 1v1 or 2 for PvAI: ")
    try:
        if choice == '1':
            gm.Player_v_Player()
        elif choice == '2':
            gm.Player_v_AI()
        else:
            raise ValueError("Wrong value")
    except IOError:
        print('Invalid Input')


if __name__ == "__main__":
    main()
