#!/usr/bin/python

import sys
import os
import hashlib
import csv
from datetime import datetime
from os import listdir, walk
from os.path import isfile, join

# used resources from programiz.com, geeksforgeeks.com, stackoverflow, newbedev.com, and github
# collaborated with 1/C Kingel

# look through directories
# list of directories to ignore - these are unhashable

ignore = ['/dev','/proc','/run','/sys','/tmp','/var/lib','/var/run']

# walk through file system, but skip the ignore list

#def hash_function():
def main():
    if os.path.isfile("hash.csv"):
        print("File exists")
        quit()
    print("----------------------Hashing----------------------")
    newfile = open("hash.csv","w")
    #f = []
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    for (root, dirnames, filenames) in walk('/'): # each directory - splits into files and dirs
        #f.extend(filenames)
        if root in ignore: # check if the directory is in the ignored list
            dirnames[:]=[] # set the entire list to an empty list
            filenames[:]=[] # in these empty lists, add the new files to be hashed
        for file in filenames: # this will iterate through all the filnames not listed in ignore
            hashfile = os.path.join(root,file) # this will be the file to be hashed
            #print(hashfile)
            try: # use try, except - there are issues trying to open certain directories
                f = open(hashfile, 'rb') # this will read the hash into binary
            except:
                f.close()
                continue
            while True:
                data = f.read(BUF_SIZE) # read in specified chunks
                if not data:
                    break
                sha256.update(data) # this will take the variable that will be hashed
            f.close()
            hashline = sha256.hexdigest() # sha256
            newfile.write(hashline) # write back into the file I originally created
    # add the date and time to the end of file
    current = datetime.now()
    dt_string = current.strftime("%d/%m/%Y %H:%M:%S")
    newfile.write(dt_string)
    print("complete.")
    print("\nLast Updated:\n")
    print(dt_string)
    newfile.close()
    quit()

main()
