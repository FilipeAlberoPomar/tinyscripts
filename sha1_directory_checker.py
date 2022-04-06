import os
import os.path
import shutil
import subprocess

dir = input("Dir>>  ")

dir_exists = os.path.isdir(dir)

if dir_exists:
    os.chdir(dir)
    for file in os.listdir(dir):
        if file.endswith(".sha1"):
            command = "shasum -c '%s'" % file
            print("\n"+command)
            os.system(command)
else:
    print("\nDir not found")

input("\npress any key")
