from hashlib import *
from datetime import datetime

#--------------------------------------- CLASS AND FUNCTIONS

class cracking_password:
    def __init__(self):
        self.__password_list = ''
        self.__hash_password = ''
        self.__hash_algorithms = ''
        self.__passwords = None
        self.__hashes_class = {
                               'md5': md5,
                               'sha1': sha1,
                               'sha224': sha224,
                               'sha256': sha256,
                               'sha384': sha384,
                               'sha512': sha512,
                               'sha3_224': sha3_224,
                               'sha3_256': sha3_256,
                               'sha3_384': sha3_384,
                               'sha3_512': sha3_512,
                               'blake2b': blake2b,
                               'blake2s': blake2s
                              }

    def start(self):
        print('start cracking passwords:\n')
        
        self.__hash_password = input('Please enter your hash password: ')
        algorithms = input('Please enter your hash algorithm: ')
        
        if not algorithms or algorithms == 'all' or algorithms == 'ALL':
            self.__hash_algorithms = ['md5',
                                      'sha1',
                                      'sha224',
                                      'sha256',
                                      'sha384',
                                      'sha512',
                                      'sha3_224',
                                      'sha3_256',
                                      'sha3_384',
                                      'sha3_512',
                                      'blake2b',
                                      'blake2s']

        else:
            for char in algorithms:
                if char == ' ':
                    continue
                self.__hash_algorithms += char
                
            self.__hash_algorithms = self.__hash_algorithms.split(',')


        mode = self.__check_file()
        if mode:
            self.__crack_password()
        
        self.__init__()

    def __check_file(self):
        choice = input('Is your password list "password list.txt" (y / n): ').lower()
        if choice == 'y' or choice == 'yes':
            self.__password_list = 'password lists//password list.txt'

        elif choice == 'n' or choice == 'no':
            self.__password_list = input('Please enter your password list path: ')

        else:
            return False

        return True
    
    def __read_file(self):
        try:
            with open(self.__password_list, 'rb') as FILE:
                for password in FILE:
                    yield password.split('\n'.encode())[0]

        except FileNotFoundError:
            print('Please check your PATH or NAME of your password list.')

        except OSError:
            print('Please check your PATH of your password list.')

        except Exception as e:
            print('Something went wrong on openning file !!!')
            print(e)
    
    def __crack_password(self):
        print('\ncracking password\nplease wait...\n')
        time = datetime.now()        
        key = 1
        for password in self.__read_file():
            for hash_algorithm in self.__hash_algorithms:
                try:
                    hashed_password = self.__hashes_class[hash_algorithm](password).hexdigest()
                except:
                    None
                else:
                    if self.__hash_password == hashed_password:
                        time1 = datetime.now()
                        print(f'\rYour Hash Password is CRACKED !!!{' ' * 50}\n')
                        print(f'Password => {password}')
                        print(f'Algorithm => {hash_algorithm}')
                        print(f'your password was the {key}th password of the passwords of {self.__password_list}\n')
                        print(f'Cracking finished on {time1-time}\n')
                        return None

            print(f'\r{key:.0f} has been passwords tested.', end='')
            key += 1

        time1 = datetime.now()
        print('\rPassword not found :(\n')
        print(f'Checking finished on {time1-time}\n')
        print('For better result you can do these:')
        print('[*] Check your hash password.')
        print('[*] Check your hash algorithms.')
        print('[*] Develop your password list.\n')

#--------------------------------------- PROGRAM
