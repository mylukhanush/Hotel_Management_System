from os import remove

from Guest import *
from Utility import *
from Room import *

class Manager :
    def __init__(self):
        self.guests = []
        self.rooms = 10

    def check_in (self):
        name = input("Enter the name: ")
        phone_number = int(input("Enter phone number: "))
        self.guests.append(name)

        print(f"WELCOME TO TALASSA :{name}")

    def list_guests(self):
        if len(self.guests) == 0:
            print("\nguest list is empty !")
            return
        else:
            for guests in self.guests:
                print(f"guest name: {guests}")

    def check_rooms(self):
        available_rooms = self.rooms - len(self.guests)
        # if len(self.guests) != 0:
        #     print("Rooms are available")
        if available_rooms <= 0:
            print("Rooms are full")
        elif available_rooms != 0 and len(self.guests)<=10:
            print(f"Only {len(self.guests)} is filled out of 10")

    def check_out (self):
        name = input("enter the name")
        for guests in self.guests:
            if guests == name:
                self.guests.remove(guests)
            print("guest removed successfully")
            break

    def price(self):
        print("price of deleux room is 5000")
        print("price of suite room is 8000")

    def foods(self):
        food_menu = ["dose","idly","vada","puri","butter chicken","roti","water bottle","soft drinks"]
        print(food_menu)
        food = input("Enter the food name :")
        if food in food_menu:
            print("Food will be delivered in 15 min")
        else:
            print("please only choose from menu")