from hashlib import *

#--------------------------------------- CLASS  AND FUNCTIONS

class hashing:
    def __init__(self):
        self.__password = ''
        self.__algorithms = ''
        self.__hashed_password = ''
        self.__hashes_class = {'md5': md5,
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
                               'blake2s': blake2s}

    def start(self):
        print('start hashing passwords:\n')

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
        file = open('Spass/history/hashed passwords.txt', 'a')
        encoded_password = self.__password.encode()
        for algorithm in self.__algorithms:
            try:
                self.__hashed_password = self.__hashes_class[algorithm](encoded_password).hexdigest()
            
            except KeyError:
                print('algorithm not found :(')
            
            else:
                file.write(f'Password: {self.__password}\nAlgorithm: {algorithm}\nHash: {self.__hashed_password}')
                file.write(f"\n\n{'-'*100}\n\n")

                print(f'Password => {self.__password}')
                print(f'Hash => {self.__hashed_password}')
                print(f'Algorithm => {algorithm}\n')
        
        file.close()
        print('stop hashing passwords :)\n')
        self.__init__()

#--------------------------------------- PROGRAM
