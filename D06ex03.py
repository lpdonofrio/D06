########################################################################
#write a function that reads from roster.txt prints the following
#information to the command line:
#   a. how many names contain the letter ‘e’
#   b. then lists the names which contain the letter ‘e’
########################################################################

#Imports

#Body
def e_names():
    with open("roster.txt", "r") as fin:
        count = 0
        list_names = []
        for line in fin:
            name_only = line.split()[0]
            if "e" in name_only or name_only.find("E") != -1:
                count += 1
                list_names.append(name_only)
        print(count)
        print(list_names)



########################################################################
def main():

    print(e_names())

if __name__ == '__main__':
    main()