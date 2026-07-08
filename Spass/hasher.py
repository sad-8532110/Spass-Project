from hashlib import *

#--------------------------------------- CLASS  AND FUNCTIONS

class hashing:
    def __init__(self):
        self.__password = ''
        self.__algorithms = ''
        self.__hashed_password = ''

    def start(self):
        print('start hashing passwords:\n')
        self.__file = open('Spass/history/hashed passwords.txt', 'a')

        self.__password = input('Please enter your password: ')
        algorithms = input('Please enter your hash algorithms: ')
        
        if not algorithms or algorithms == 'all' or algorithms == 'ALL':
            self.__algorithms = ['md5',
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
                self.__algorithms += char
            self.__algorithms = self.__algorithms.split(',')

        self.__make_hashed_password()

    def __make_hashed_password(self):
        print()
        for algorithm in self.__algorithms:
            if algorithm == 'md5' or algorithm == '1':
                algorithm = 'md5'
                self.__hashed_password = md5(self.__password.encode()).hexdigest()

            elif algorithm == 'sha1' or algorithm == '2':
                algorithm = 'sha1'
                self.__hashed_password = sha1(self.__password.encode()).hexdigest()

            elif algorithm == 'sha224' or algorithm == '3':
                algorithm = 'sha224'
                self.__hashed_password = sha224(self.__password.encode()).hexdigest()

            elif algorithm == 'sha256' or algorithm == '4':
                algorithm = 'sha256'
                self.__hashed_password = sha256(self.__password.encode()).hexdigest()

            elif algorithm == 'sha384' or algorithm == '5':
                algorithm = 'sha384'
                self.__hashed_password = sha384(self.__password.encode()).hexdigest()

            elif algorithm == 'sha512' or algorithm == '6':
                algorithm = 'sha512'
                self.__hashed_password = sha512(self.__password.encode()).hexdigest()

            elif algorithm == 'sha3_224' or algorithm == '7':
                algorithm = 'sha3_224'
                self.__hashed_password = sha3_224(self.__password.encode()).hexdigest()

            elif algorithm == 'sha3_256' or algorithm == '8':
                algorithm = 'sha3_256'
                self.__hashed_password = sha3_256(self.__password.encode()).hexdigest()

            elif algorithm == 'sha3_384' or algorithm == '9':
                algorithm = 'sha3_384'
                self.__hashed_password = sha3_384(self.__password.encode()).hexdigest()

            elif algorithm == 'sha3_512' or algorithm == '10':
                algorithm = 'sha3_512'
                self.__hashed_password = sha3_512(self.__password.encode()).hexdigest()

            elif algorithm == 'blake2b' or algorithm == '11':
                algorithm = 'blake2b'
                self.__hashed_password = blake2b(self.__password.encode()).hexdigest()

            elif algorithm == 'blake2s' or algorithm == '12':
                algorithm = 'blake2s'
                self.__hashed_password = blake2s(self.__password.encode()).hexdigest()

            else:
                algorithm = 'invalid algorithm'
                self.__hashed_password = 'invalid hash'

            self.__file.write(f'Password: {self.__password}\nAlgorithm: {algorithm}\nHash: {self.__hashed_password}')
            self.__file.write(f"\n\n{'-'*100}\n\n")

            print(f'Password => {self.__password}')
            print(f'Hash => {self.__hashed_password}')
            print(f'Algorithm => {algorithm}\n')
        
        self.__file.close()
        print('stop hashing passwords :)\n')
        self.__init__()

#--------------------------------------- PROGRAM

