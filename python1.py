from audioop import add

import string
from traceback import print_tb
import numpy as np
import random
import datetime
from datetime import timedelta
import os
import pandas as pa


def packages():
    print("""
    Packages that We Offer
          1.Luxury Room
            These cozy windowless rooms located in the historic Palace Wing offer you complete tranquillity.

          2.Luxury Grande Room City View
            These rooms are located in the Palace Wing on the 2nd, 3rd and 4th floors.

          3.Luxury Grande Room Sea View
            These rooms offer spectacular views of the Arabian Sea or the Gateway of India.

          4.The Tata Suite
            Created in the honor of our Founder with extravagance of lush carpets and fine architectural detailing.

            (Note - All Packages include Complimentary Wifi Service ,King size bed can accomodate upto 3 guests.)
            To Check Price of Packages Enter 1
          """)
    g = int(input())
    if g == 1:
        print("""
              (Note - Starting Rate/Night)

              1.Luxury Room                      Rs.4000*
              2.Luxury Grande Room City View     Rs.7000*
              3.Luxury Grande Room Sea View      Rs.10000*
              4.The Tata Suite                   Rs.15000*
              """)
        selectpackage()
    else:
        quit()


def selectpackage():
    print("Please select package")
    global select
    select = int(input())
    print("For how many nights you are willing to stay")
    global night
    night = int(input())
    global packagename
    if select == 1:
        packagename = "Luxury Room"
        arr = np.array(
            [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120])
        arr1=np.random.choice(arr, size=3, replace=False)
        a=arr1
    elif select == 2:
        packagename = "Luxury Grande Room City View"
        arr = np.array(
            [201, 203, 205, 207, 208, 209, 210, 212, 213, 214, 223, 312, 354, 316, 359, 333, 327, 369, 330, 342, 360,
             364, 421, 456, 412, 489, 423, 410, 412, 432, 465, 474, 416])
        arr2=np.random.choice(arr, size=5, replace=False)
        a=arr2
    elif select == 3:
        packagename = "Luxury Grande Room Sea View"
        arr = np.array([706, 704, 752, 746, 712, 795, 734, 761, 792, 749, 768, 713, 741])
        arr3=np.random.choice(arr, size=3, replace=False)
        a=arr3
    elif select == 4:
        packagename = "The Tata Suite"
        arr = np.array([906, 904, 952, 946, 912, 995, 934, 961, 992, 949, 968, 913, 941])
        arr4=np.random.choice(arr, size=3, replace=False)
        a=arr4
    print("We have These three rooms available right now,please select one")
    global roomnumber
    roomnumber = int(6)

    while roomnumber not in a:
        print(a)
        roomnumber = int(input())

        if roomnumber not in a:
            print("Wrong room number , enter correct one")



    global roomrent
    if select == 1:
        roomrent = 4000 * night
    elif select == 2:
        roomrent = 7000 * night
    elif select == 3:
        roomrent = 10000 * night
    elif select == 4:
        roomrent = 15000 * night

    print("Your Room number is ", roomnumber)
    print("Your Room Rent Rs.", roomrent)


def customerinfo():
    print("Enter Customer Details \n")
    print("Enter Customer Name")
    global name
    name = input()
    print("enter customer email id")
    global email
    email = input()
    print("enter customer phone number")
    global phone
    phone = input()
    print("enter customer's address")
    global address
    address = input()


def checkcustomer():
    print("Customer Details ")
    print("Customer Name :", name)
    print("Customer email id :", email)
    print("Customer phone number :", phone)
    print("Customer's address :", address)


def checkroom():
    print("Room Details")
    print("Package Name :", packagename)
    print("Room Number :", roomnumber)
    print("Room Rent :", roomrent)


def makepayment():
    global allbill
    print("Your Total Bill is : ",allbill)
    print("please select payment mode")
    print("1.Pay by cash")
    print("2.Pay Online")
    b = int(input())
    if b == 1:
        print("")
    elif b == 2:
        print("1.Credit/Debit Card")
        print("2.UPI")
        print("3.Scan The QR Code")

        print("please select payment options")
        d = int(input())
        if d == 1:
            print("Enter 16 digit Card Number")
            cardnumber = input()
            print("Expiry Date :(MM/YY)")
            expirydate = input()
            print("enter 3 digit CVV :")
            cvv = input()
        elif d == 2:
            print("please enter UPI ID")
        elif d == 3:
            print("please scan the QR code")

    print("if payment done press 1")
    c = int(input())
    if c == 1:
        print("Thank you for payment")
    else:
        print("You have to make payment to buy a room")


def food():
    print("ORDER YOUR FOOD:")
    dc = input('YOU WANT DRINK ? YES OR NO\n')

    drinkbill = 0
    maincourse_bill = 0
    total_mc = 0
    total_d = 0
    if dc == "YES":
        print("---------------- DRINKS -----------------")
        print("""    
            1)Cola          20rs
            2)Nestea        30rs
            3)Sprite        40rs
            4)Mojito        60rs
            5)Gin tonic     60rs
            6)Whiskey       300rs
            """)

        z = "YES"
        while (z == "YES"):
            w = int(input("ENTER YOUR CHOICE NO"))

            q = int(input("quantity"))
            if w == 1:
                drinkbill = 20 * q
            elif w == 2:
                drinkbill = 30 * q
            elif w == 3:
                drinkbill = 40 * q
            elif w == 4:
                drinkbill = 60 * q
            elif w == 5:
                drinkbill = 60 * q
            elif w == 6:
                drinkbill = 300 * q

            total_d = total_d + drinkbill

            print("do you want to buy more")
            z = input()

    mc = input('YOU WANT MAIN COURSE ? YES OR NO\n')
    if mc == "YES":
        print("---------------- MAIN COURSE -----------------")
        print("""
            1)PANEER             300rs
            2)KAJU CURRY         300rs
            3)PANNER MASALA      350rs
            4)KAJU MASALA        350rs
            5)PASTA              300rs
            6)MALAI KOFTA        400rs
            7)VEG PARATHA        350rs      
        """)
        y = "YES"
        while (y == "YES"):
            e = int(input("ENTER YOUR CHOISE NO"))
            d = int(input("quantity"))
            if e == 1:
                maincourse_bill = 300 * d
            elif e == 2:
                maincourse_bill = 300 * d
            elif e == 3:
                maincourse_bill = 350 * d
            elif e == 4:
                maincourse_bill = 350 * d
            elif e == 5:
                maincourse_bill = 300 * d
            elif e == 6:
                maincourse_bill = 400 * d
            elif e == 7:
                maincourse_bill = 350 * d

            total_mc = total_mc + maincourse_bill

            print("do you want to buy more")
            y = input()

    global bill
    bill = total_mc + total_d
    print('your food bill is :')

    print(bill)


def receipt():
    print("-------------------- BILL RECEIPT ----------------------")
    print("--------------------------------------------------------")
    print("Branch : Nagpur")
    x = datetime.datetime.now()
    print("Check In Date:\t", x.strftime("%c"))
    y = x + timedelta(days=(night + 1))
    print("Check Out Date:\t", y.strftime("%c"))
    print("Customer Detalis :")
    print("--------------------------------------------------------")
    print("Customer Name:\t\t\t\t\t", name)
    print("Customer Email ID:\t\t\t\t", email)
    print("Customer Phone Number:\t\t\t\t", phone)
    print("Customer Address:\t\t\t\t", address)
    print("--------------------------------------------------------")
    print("Package Name :", packagename)
    print("Room Number :", roomnumber)
    print("--------------------------------------------------------")
    print("Total Services And its Cost :")
    print("Room Rent\t\t\t\t", roomrent)
    print("Food Bill\t\t\t\t", bill)
    print("Gaming Bill\t\t\t\t",total_gc )
   # print("Gaming Bill\t\t\t\t", sum2)
    print("--------------------------------------------------------")
    global allbill
    allbill=roomrent+bill+total_gc
    print("Grand Total\t\t\t\t", allbill)


def game():
    global gamingcost
    gamingcost = 0
    global total_gc
    total_gc = 0
    print("""
            (Prices mentioned as per hour)\n
            1.Table tennis          Rs.120
            2.Bowling               Rs.200
            3.Snooker               Rs.120
            4.Video games           Rs.100
            5.Pool                  Rs.150
            6.Exit""")

    while (1):

        g = int(input("Enter your choice:"))

        if (g == 1):
            h = int(input("No. of hours:"))
            gamingcost = 120 * h

        elif (g == 2):
            h = int(input("No. of hours:"))
            gamingcost = 200 * h

        elif (g == 3):
            h = int(input("No. of hours:"))
            gamingcost = 120 * h

        elif (g == 4):
            h = int(input("No. of hours:"))
            gamingcost = 100 * h

        elif (g == 5):
            h = int(input("No. of hours:"))
            gamingcost = 150 * h
        elif (g == 6):
            break;

        else:

            print("Invalid option")

        total_gc = total_gc + gamingcost

    print("""
               Total Gaming Cost           Rs""",total_gc , "\n")


def query():
    print("If You have Any Query Regarding Bill receipt or hotel management ,feel free to contact")

    j = pa.read_csv('Book1.csv', sep='[:, |_]', engine='python')
    print(j.to_string())


def main():
    global bill
    bill=0
    global gamingcost
    gamingcost = 0
    global total_gc
    total_gc = 0
    global allbill
    allbill=0
    print("""
            --------------------------------------------------------------
            -------------- WELCOME TO GALAXY HOTEL, NAGPUR ---------------
            --------------------------------------------------------------
            """)

    packages()
    customerinfo()
    o = "1"
    while o != 8:
        print("1.Check Customer Details")
        print("2.Check Room Details")
        print("3.Food Menu")
        print("4.Game Parlour")
        print("5.Bill Receipt")
        print("6.Regarding Query")
        print("7.Make Payment")
        print("8.Exit")
        print("\nSelect Services")
        o = int(input())
        if o == 1:
            checkcustomer()
            print("\n")
        elif o == 2:
            checkroom()
            print("\n")
        elif o == 3:
            food()
            print("\n")
        elif o == 4:
            game()
            print("\n")
        elif o == 5:
            receipt()
            print("\n")
        elif o == 6:
            query()
            print("\n")
        elif o == 7:
            makepayment()
            print("\n")
        elif o == 8:
            quit()


main()