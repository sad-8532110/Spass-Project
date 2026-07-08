from random import sample

#--------------------------------------- CLASS AND FUNCTIONS

class make_password:
    def __init__(self):
        self.__password_lenght = 0
        self.__password_count = 0

    def start(self):
        try:
            print('start making passwords:\n')
            
            self.__file = open('Spass/history/generated passwords.txt', 'a')
            self.__file.write('Passwords:\n\n')

            self.__password_lenght = int(input('Please enter your password lenght: '))
            self.__password_count = int(input('How many password do you want to have: '))

            self.__make_password()

        except ValueError:
            print('\nPlease check your input.\n')

    def __make_password(self):
        all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-+*`~!@#$%^&()_=><,?;:[]{}|'

        print()
        for i in range(self.__password_count):
            self.__password = ''.join(sample(all_chars, self.__password_lenght))
            
            self.__file.write(self.__password + '\n')
            print(self.__password)

        self.__file.write('\n' + '-' * 100 + '\n\n')
        self.__file.close()
        
        print('\nstop making passwords :)\n')

#--------------------------------------- PROGRAM
