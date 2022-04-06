import os
import os.path
import shutil
import subprocess

HARD_CODED_PASSWORD = ""

MAIN_MENU = """
-------------------------
   Archivator Tabajara
-------------------------
1. Validate file
2. Validate directory
3. Archive a directory
0. Exit\n"""

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

def validate_file():
    os.system("clear")
    file = input("File>>  ")

    file_exists = os.path.isfile(file)

    if file_exists:
        dirname = os.path.dirname(file)
        filename = os.path.basename(file)
        os.chdir(dirname)
        command = "shasum -c '%s.sha1'" % filename
        os.system(command)
    else:
        print("\nFile not found")

    input("\npress any enter")
    os.chdir(BASE_PATH)
    main_menu()


def validate_directory():
    os.system("clear")
    dir = input("Dir>>  ")

    dir_exists = os.path.isdir(dir)

    if dir_exists:
        os.chdir(dir)
        for file in os.listdir(dir):
            if file.endswith(".tar.gz") or file.endswith(".enc"):
                command = "shasum -c '%s.sha1'" % file
                print("\n"+command)
                os.system(command)
    else:
        print("\nDir not found")

    input("\npress any key")
    os.chdir(BASE_PATH)
    main_menu()


def archive_directory():
    # os.system("clear")
    # password = input("Password>>  ")

    #if password == HARD_CODED_PASSWORD:
    dir_path = input("Dir>>  ")
    dir_exists = os.path.isdir(dir_path)

    if dir_exists:
        if not dir_path.endswith(os.sep):
            dir_path = dir_path + os.sep # need a slash at the end to extract dir_name properly

        # Declaration of variables needed later
        dirname = os.path.dirname(dir_path)
        dir_temp = dirname+"-temp"
        tar = dirname+".tar.gz"
        tar_encrypted = tar+".enc"
        tar_decrypted = dirname+"-temp.tar.gz"

        print("\nCOMPRESSING ")
        # tar -czf "$TAR" "$DIR"
        command = "tar -czf '%s' -C '%s' ." % (tar, dirname)
        print(command)
        os.system(command)

        print("\nGENERATING CHECKSUM")
        # shasum "$TAR" > "$TAR.sha1"
        command = "shasum '%s' > '%s.sha1' " % (tar, tar)
        print(command)
        os.system(command)

        print("\nENCRYPTING")
        # openssl enc -aes-256-cbc -a -salt -in "$TAR" -out "$TAR_ENCRYPTED" -pass pass:"$PASSWORD"
        command = "openssl enc -aes-256-cbc -a -salt -in '%s' -out '%s' -pass pass:'%s'" % (tar, tar_encrypted, HARD_CODED_PASSWORD)
        print(command)
        os.system(command)

        print("\nGENERATING CHECKSUM")
        command = "shasum '%s' > '%s.sha1'  " % (tar_encrypted, tar_encrypted)
        print(command)
        os.system(command)

        # REVERSING OPERATIONS FOR VALIDATION

        print("\nVALIDATING ENCRYPTION")
        # openssl enc -d -aes-256-cbc -a -in "$TAR_ENCRYPTED" -out "$TAR_DECRYPTED" -pass pass:"$PASSWORD"
        command = "openssl enc -d -aes-256-cbc -a -in '%s' -out '%s' -pass pass:'%s'" % (tar_encrypted, tar_decrypted, HARD_CODED_PASSWORD)
        print(command)
        os.system(command)

        print("\nVALIDATING COMPRESSION")
        os.makedirs(dir_temp)
        # tar xzf  "$TAR_DECRYPTED" --directory "$TMP_DIR"
        command = "tar xzf  '%s' --directory '%s'" % (tar_decrypted, dir_temp)
        print(command)
        os.system(command)

        print("\nVALIDATING CONTENT")
        command = "diff -rq '%s' '%s'" % (dirname, dir_temp)
        print(command)
        result = os.system(command)

        print("\nDELETING TEMPORARY FILES")
        command = tar_decrypted
        print(command)
        os.remove(tar_decrypted)

        command = dir_temp
        print(command)
        shutil.rmtree(dir_temp)

        if result == 0:
            print("\nSuccessful archiving")
        else:
            print("\nFailure at archiving")

    else:
        print("\nDir not found")

     #else:
    #    print("\nPasswords do not match")
    input("\npress any key")
    main_menu()

def main_menu():
    os.system("clear")
    print(MAIN_MENU)
    choice = input(">>  ")

    try:
        MENU_ACTIONS[choice]()
    except KeyError:
        main_menu()

MENU_ACTIONS = {
    '1': validate_file,
    '2': validate_directory,
    '3': archive_directory,
    '0': exit
}

if __name__ == '__main__':
    main_menu()
