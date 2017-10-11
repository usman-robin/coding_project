import os
import pprint



def main():
    print(print_dirctory_contents("/Users/usmansaeed/practice"))

def print_dirctory_contents(sPath):

    print (os.listdir(sPath))
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_dirctory_contents(sChildPath)
        else:
            print(None)



if __name__ == '__main__':
    #print("hello")
    main()