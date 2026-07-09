from hashlib import *
import os

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
        self.__algorithm_keys = list(self.__hashes_class.keys())


    def start(self):
        print('start hashing passwords:\n')

        self.__password = input('Please enter your password: ')

        print("Select Your hashing method:\n")

        for i, name in enumerate(self.__algorithm_keys, start=1):
            print(f"{i:2}. {name}")

        print("\nSeparate them with comma.")

        algorithms = input(
            "Please enter your hash algorithms: "
        ).strip()

        if not algorithms or algorithms.lower() == "all":
            self.__algorithms = self.__algorithm_names.copy()
        else:
            selected = []

            for item in algorithms.split(","):
                item = item.strip()

                if item.isdigit():
                    index = int(item) - 1

                    if 0 <= index < len(self.__algorithm_keys):
                        selected.append(self.__algorithm_keys[index])
                    else:
                        print(f"Unknown number: {item}")

                elif item in self.__hashes_class:
                    selected.append(item)

                else:
                    print(f"Unknown algorithm: {item}")

        self.__algorithms = list(dict.fromkeys(selected))

        self.__make_hashed_password()

    def __make_hashed_password(self):
        print()
        os.makedirs('Spass/history', exist_ok=True)  # create dir if it's missing
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
