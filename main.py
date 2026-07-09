from sys import stdout
from time import sleep
from pyfiglet import figlet_format
from Spass import *

#--------------------------------------- CLASS AND FUNCTIONS

class main:
    def __init__(self):
        self.__password_maker = make_password()
        self.__password_hasher = hashing()
        self.__password_cracker = cracking_password()
        
    def run_program(self):
        text = '''Hello Dear User !
Welcome to Spass

This program is for providing password services

Please choose one of these options:\n'''
        
        print(figlet_format('Spass') + '\n')
        for i in text:
            sleep(0.05)
            stdout.write(i)
            stdout.flush()
        print('''
1. hashing
2. make password
3. password crack
4. help
5. enter none to exit
''')
        mode = self.__get_choice()
        while mode:
            mode = self.__get_choice()

    def __get_choice(self):
        main_choice = input('Please enter an option: ')
        if main_choice == 'hashing' or main_choice == '1':
            self.__password_hasher.start()

        elif main_choice  == 'make password' or main_choice == '2':
            self.__password_maker.start()

        elif main_choice == 'password crack' or main_choice == '3':
            self.__password_cracker.start()

        elif main_choice == 'help' or main_choice == '4':
            self.help()

        else:
            exit_choice = input('Do you want to exit [y/N]: ').lower()
            if exit_choice == 'y' or exit_choice == 'yes':
                return False
            
        return True

    def help(self):
        print('''This program can help you in password services:

like:

password cracking
password hashing
making password\n''')
        print('''
the algorithm of hashing:
1. sha1
2. md5
3. sha256
4. sha224
5. sha384
6. sha512
7. sha3_224
8. sha3_256
9. sha3_384
10. sha3_512
11. blake2b
12. blake2s
''')

#--------------------------------------- PROGRAM

if __name__ == '__main__':
    obj = main()
    obj.run_program()
