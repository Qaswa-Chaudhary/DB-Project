from config.config import connect_db
from Models import *
from controllers import *
from views.view import views

def main():
    print('Welcome to Hotel Management System')
    print('\nMake your choice')
    print('1. Employee')
    print('2. Guests')

    choice = input('Enter your choice:')

    view = views()

    if choice == '1':
        print('Welcome')
        print('\nMake Choice')
        print('1. Booking Dtails')
        print('2. Payment History')
        print('3. Guest Service')

        emp_choice = input('Enter Your Choice:')

        if emp_choice == '1':
            data = view.view_booking_details()
            for row in data:
                print(row)

        elif emp_choice == '2':
            data = view.view_payment_history()
            for row in data:
                print(row)

        elif emp_choice == '3':
            data = view.Service_used()
            for row in data:
                print(row)

        else:
            print('Invalid Choice for Employee')

    elif choice == '2':
        print('We are warmly welcome to our Hotel')
        print('\nMake Choice')
        print('1. Guest Service')
        print('2. Payment History')

        guest_choice = input('Enter Your choice:')

        if guest_choice == '1':
            data = view.Service_used()
            for row in data:
                print(row)

        elif guest_choice == '2':
            data = view.view_payment_history()
            for row in data:
                print(row)
        
        else:
            print('Invalid Choice for Guest')

    else:
        print('invalid choice')


if __name__ == '__main__':
    main()

