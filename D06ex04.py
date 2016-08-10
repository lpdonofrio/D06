########################################################################
#Modify script from problem D06ex03 to write results to a file
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
        return count, list_names


def write_to_file():
    count_names, names_list = e_names()
    with open("names_with_e.txt", "w") as fout:
        fout.write(str(count_names) + " names contain the letter 'e': \n")
        for name in names_list:
            fout.write(name + "\n")





########################################################################
def main():

    write_to_file()

if __name__ == '__main__':
    main()