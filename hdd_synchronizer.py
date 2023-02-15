import os
from datetime import datetime

MAC_MASTER = """rsync
--dry-run
--archive
--verbose
--progress
--human-readable
--delete
--exclude=".*"
--exclude ".*/"
--exclude=Applications
--exclude=Downloads
--exclude=Library
--exclude=Movies
--exclude=Music
--exclude=Public
--exclude=Acervo
~/
/Volumes/MASTER/Mac/""".replace('\n',' ')

MASTER_COPYOFMASTER = """rsync
--dry-run
--archive
--verbose
--progress
--human-readable
--delete
--exclude=".*"
--exclude ".*/"
--exclude "_bkp_*"
/Volumes/MASTER/
/Volumes/COPYOFMASTER/""".replace('\n',' ')

MASTER_MEDIA = """rsync
--dry-run
--archive
--verbose
--progress
--human-readable
--delete
--exclude=".*"
--exclude ".*/"
/Volumes/MASTER/Media/
/Volumes/MEDIA/Media/""".replace('\n',' ')

MAIN_MENU = """
---------------------------
%s
---------------------------
1. Mac > Master
2. Master > CopyOfMaster
3. Master > Media
0. Exit\n"""

SUB_MENU = """
---------------------------
%s
---------------------------
1. Dry Run 
2. Synchronize
0. Back\n"""


def main_menu():
    os.system("clear")
    print(MAIN_MENU % "   Synchronizer Tabajara")
    choice = str(input(">>  "))

    try:
        MAIN_ACTIONS[choice]()
    except KeyError:
        main_menu()


def mac_master():
    os.system("clear")
    print(SUB_MENU % "       MAC > MASTER")
    choice = str(input(">>  "))

    if choice == "1":
        os.system(MAC_MASTER)
    elif choice == "2":
        os.system(MAC_MASTER.replace("--dry-run", ""))
        timestamp = datetime.now().strftime("%Y-%m-%d@%H.%M")
        os.system("touch /Volumes/Master/_bkp_mactomaster_%s" % timestamp)
    elif choice == "0":
        main_menu()

    input("\npress any enter")
    mac_master()

def master_copyofmaster():
    os.system("clear")
    print(SUB_MENU % "   MASTER > COPYOFMASTER")
    choice = str(input(">>  "))

    if choice == "1":
        os.system(MASTER_COPYOFMASTER)
    elif choice == "2":
        os.system(MASTER_COPYOFMASTER.replace("--dry-run", ""))
        timestamp = datetime.now().strftime("%Y-%m-%d@%H.%M")
        os.system("touch /Volumes/CopyOfMaster/_bkp_mastertocopyofmaster_%s" % timestamp)
    elif choice == "0":
        main_menu()

    input("\npress any enter")
    master_copyofmaster()


def master_media():
    os.system("clear")
    print(SUB_MENU % "     MASTER > MEDIA ")
    choice = str(input(">>  "))

    if choice == "1":
        os.system(MASTER_MEDIA)
    elif choice == "2":
        os.system(MASTER_MEDIA.replace("--dry-run", ""))
    elif choice == "0":
        main_menu()

    input("\npress any enter")
    master_media()


MAIN_ACTIONS = {
    '1': mac_master,
    '2': master_copyofmaster,
    '3': master_media,
    '0': exit
}

if __name__ == '__main__':
    main_menu()
