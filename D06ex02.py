########################################################################
#Write ten random numbers to a file
########################################################################

#Imports
import random

#Body
def write_file():
    with open("ten_random_numbers.txt", "w") as fin:
        for n in range(1, 11):
            fin.write(str(random.randint(1, 100)) + "\n")

########################################################################
def main():

    print(write_file())

if __name__ == '__main__':
    main()