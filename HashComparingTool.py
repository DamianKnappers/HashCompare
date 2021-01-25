# Hash Comparing Tool
import os
import hashlib

def checkFromInput():
    try:
        inputhash = str(input("What's the hash?: "))
        tocheck = "(Static Set MD5 Hash here)"
        if inputhash == tocheck:
            print("Hash is the same!!")
        else:
            print("Not the same!")
            main()


    except KeyboardInterrupt:
        print("Quiting")
        
def checkFromFile():
    try:
        tocheck = input("MD5 Hash: ")
        BDirs = "hashes.txt"
        path = str(os.getcwd()+ "\\" +  BDirs)
        tFile = open(path,"r")
        file = tFile.readlines()
        i = 0
        for line in file:
            hs = file[i]
            hashes = hashlib.md5(hs.encode())
            if hashes == tocheck:
                print("[+] Hash checks out: " + hashes)
            else:
                print("[-] Not the same!: " + hashes)
            i = i + 1
    except KeyboardInterrupt:
        print("Quiting... HoLD ON!")
def main():
    try:
        choice = int(input("1 = From Input / 2 = From File?: "))
        if choice == 1:
            checkFromInput()
        elif choice == 2:
            checkFromFile()
        else:
            print("Give me the correct number!!")
    except ValueError():
        print("So you are giving me a wrong type of input god dammit!")
            
main()
