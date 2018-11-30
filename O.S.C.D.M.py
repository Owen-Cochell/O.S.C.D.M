import time
import os
import itertools
import threading
import sys
import subprocess
import platform

# A Disk Manager useing the SSHFS Protocol

ogPath = os.path.dirname(os.path.realpath(__file__))
os.system('color 0a')
name = ''
username = ''
purpose = ''
threeBit = False
sixBit = False
ip = 'lola.myftp.biz'
done = None
ver = '1.0.0'
drive = 'Z'
port = 8299
yes = ('y', 'Y', 'yes', 'Yes', 'YES', 'ye', 'Ye')
no = ('n', 'N', 'no', 'No', 'NO')
sti = ''

def clear():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def get_download_path():
    #Some great code here, did not write this!:
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def exitTime(ogPath):

    os.chdir(ogPath)
    os.system('del /F null')
    exit()

def ping(ip, bug=False):

    pingstat = None
    #Function for testing PING connectivity
    print("\nChecking connectivity to servers...")
    if bug:

        pingstat = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + ip)
        print('')

    else:
        
        pingstat = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + ip + ">null")
    
    if pingstat != 0:

        print("Host {} is down!\nDiagnossing...".format(ip))
        pingdiag(ip)
        return
        
    print("Host {} is up!".format(ip))
    
    if bug:

        empty = input("\nPress enter to continue...")
        
    return

def pingLoop(ip):

    clear()
    while True:

        pingstat = None
        print("Testing connectivity to servers...")
        pingstat = os.system("ping " + ("-n 5 " if  platform.system().lower()=="windows" else "-c 5 ") + ip + ">null")
        
        if pingstat == 0:

            clear()
            print("\n+=============================================================+")
            print("Recived response from server!")
            print("Please be aware that the host {} may not be ready for a connection yet.".format(ip))
            print("Just because a system has internet dose not mean it is in a stable state.")
            print("Please wait for instructions from Owen Cochell before procedeing!")
            empty = input("\nPress enter to continue...")
            return

        elif pingstat != None:

            print("Connectivity test failed :(")
            print("Waiting 30 seconds then re-trying...")
            time.sleep(30)
            continue
        

def pingdiag(ip):
    
    pingstat = None
    print("\nAttempting to try again(This time with more packets!)...\n")
    pingstat = os.system("ping " + ("-n 4 " if  platform.system().lower()=="windows" else "-c 4 ") + ip + ">null")
    
    if pingstat == 0:
        
        print("\nHost {} is up!".format(ip))
        print("Must have been a false alarm or slow connection...\nContinuing!!!!!")
        time.sleep(2)
        return
    
    elif pingstat != None:
        
        print("\nFailed to connect to {} A second time!".format(ip))
        print("Might be a network error. Trying a general PING test...\n")
        print("Testing PING for: Google")
        pingstat = os.system("ping " + ("-n 4 " if  platform.system().lower()=="windows" else "-c 4 ") + 'google.com' + ">null")
        
        if pingstat == 0:
            
            print("\n+====================================================+")
            print("\nHost Google(Domain: google.com) is UP!")
            print("This is NOT a network error. Something is wrong with the receiving end(Host: {})".format(ip))
            print("This is an issue on Owen's end, (probably)NOT YOURS!")
            print("Please contact Owen Cochell, and alert him that their is an issue.")
            print("The error could be a number of things, so it may take some time before the service is back up.")
            print("This script will continue to check every thirty seconds for a connection.")
            print("Feel free to close the window at any time, no damage will be done!")
            empty = input("\nPress any key to continue...")
            pingLoop(ip)
            return
        
        elif pingstat != None:
            
            print("\n+===========================================================+")
            print("Host Google(Domain: google.com) is DOWN!")
            print("This means their is proabbly an issue with your wifi, or your DNS configuration.")
            print("I mean, the chances of Google being down for any amount of time is slim to none.")
            print("Check ALL cables, and check the router.")
            print("Be sure to check your system as well. Perhapps their is something wrong.")
            print("If you have any questions, you can contact Owen Cochell.")
            print("This script will now close, as their is no need to keep checking if the wifi is down")
            empty=input("\nPress any key to exit...")
            exitTime(ogPath)

def insts(threeBit, sixBit, no):

    #Function for checking user installs
    print("Checking user instillations...")
    
    if os.path.isdir('C:\Program Files (x86)\SSHFS-Win'):
        
        print("32-Bit instillation found under 'C:\Program Files (x86)\SSHFS-Win'!")
        os.chdir('C:\\Program Files (x86)\\SSHFS-Win\\bin\\')
        threeBit=True
        return threeBit
    
    if os.path.isdir('C:\Program Files\SSHFS-win'):
        
        print("64-Bit instillation found under 'C:\Program Files\SSHFS-win'!")
        os.chdir('C:\\Program Files\\SSHFS-Win\\bin\\')
        sixBit=True
        return sixBit
    
    else:

        print("SSHFS-Win instillation not found :(")
        print("Installing and configuring SSHFS-Win instillation...")
        #Code for instillation here:
        installProg(no)
        return

def installProg(no):

    while True:
        
        clear()
        location = ''
        #Changing directory to downloads foulder:
        location = get_download_path()
        os.chdir(location)
        print("\nThis script will install the following programs:")
        print("\nSSHFS-Win:\nhttps://github.com/billziss-gh/sshfs-win")
        print("\nWinFsp:\nhttps://github.com/billziss-gh/winfsp/tree/v1.3")
        print("\nPlease look over these programs\nYou can contact Owen Cochell if you have any questions.")
        
        print("Would you like the 32bit version or the 64bit version?:\n[1]: 32bit(Recommended)\n[2]: 64bit")
        try:
        
            instInp = int(input("\nEnter a number:"))

        except:

            print("\nNaughty Naughty Naughty!\n")
            print("You tried to enter a letter, when I specificly said to enter a number!")
            print("Shame on you. You should be ashamed of yourself.")
            empty = input("\nPress ENTER(And only enter!) to continue...")
            continue

        print("\nAre you sure you want to install these programs?:")
        conf = input("\n(Y/N):")
        
        if conf in no:

            print("Exiting...")
            exitTime(ogPath)

        #Getting programs:
        
        if instInp == 1:

            #Installing 32bit version
            clear()
            print("+======================================================+")
            print("Lots of windows will open. Don't worry, that is normal.")
            print("If this scrip unexpectidly exits, worry not!")
            print("Just navigate to your download foulder and run the .MSI files that were downloaded.")
            print("Or, you can manualy go to the websites listed above and download them there if you prefer.")
            print("Accept all default options on the installers.")
            print("\nIMPORTANT:\nYou may see a window appear upon trying to run the installer for SSHFS-Win that is warning the user of potentially harmefull software.")
            print("This is a false positive. The SSHFS-Win program containes no malicious code!")
            try:
                
                os.system('start https://github.com/billziss-gh/sshfs-win/releases/download/v2.7.17334/sshfs-win-2.7.17334-x86.msi')
                os.system('start https://github.com/billziss-gh/winfsp/releases/download/v1.3/winfsp-1.3.18160.msi')
                print("\nThe programs may take some time to install depending on your connection.")
                print("Please wait untill the programs are downloaded before you continue.")
                empty = input("\nPress enter to continue...")
                os.system('start winfsp-1.3.18160.msi')
                os.system('start sshfs-win-2.7.17334-x86.msi')

            except:

                print("\nThe instillation has failed!")
                print("Try manually installing the programs from these two locations:")
                print("\nSSHFS-Win:\nhttps://github.com/billziss-gh/sshfs-win")
                print("\nWinFsp:\nhttps://github.com/billziss-gh/winfsp/tree/v1.3")
                empty = input("Press enter to exit...")
                exitTime(ogPath)

            print("\nFiles successfully installed!")
            print("Accept all default options on the installer, and the restart this scrip once complete!")
            empty = input("Press enter to exit...")
            exitTime(ogPath)

        elif instInp == 2:

            #installing 64bit version
            clear()
            print("+======================================================+")
            print("Lots of windows will open. Don't worry, that is normal.")
            print("If this scrip unexpectidly exits, worry not!")
            print("Just navigate to your download foulder and run the .MSI files that were downloaded.")
            print("Or, you can manualy go to the websites listed above and download them there if you prefer.")
            print("Accept all default options on the installers.")
            print("\nIMPORTANT:\nYou may see a window appear upon trying to run the installer for SSHFS-Win that is warning the user of potentially harmefull software.")
            print("This is a false positive. The SSHFS-Win program containes no malicious code!")
            try:
                
                os.system('start https://github.com/billziss-gh/sshfs-win/releases/download/v2.7.17334/sshfs-win-2.7.17334-x64.msi')
                os.system('start https://github.com/billziss-gh/winfsp/releases/download/v1.3/winfsp-1.3.18160.msi')
                print("The programs may take some time to install depending on your connection.")
                print("Please wait untill the programs are downloaded before you continue.")
                empty = input("\nPress enter to continue...")
                os.system('start winfsp-1.3.18160.msi')
                os.system('start sshfs-win-2.7.17334-x64.msi')

            except:

                print("\nThe instillation has failed!")
                print("Try manually installing the programs from these two locations:")
                print("\nSSHFS-Win:\nhttps://github.com/billziss-gh/sshfs-win")
                print("\nWinFsp:\nhttps://github.com/billziss-gh/winfsp/tree/v1.3")
                empty = input("Press enter to exit...")
                exitTime(ogPath)
                
            print("\nFiles successfully installed!")
            print("You system is now ready to connect to a share over the SSHFS protocol!")
            print("How exciting!")
            print("Please restart this script to continue!")
            empty = input("Press enter to exit...")
            exitTime(ogPath)

        else:

            print("Invalid option! Please enter the number of your option.")
            empty = input("Press enter to continue...")
            continue

def banner():

    #Startup Banner
    print("+=================================================+")
    print("   ____   _____  ______  ____    __  ___")
    print("  / __ \ / ___/ / ____/ / __ \  /  |/  /")
    print(" / / / / \__ \ / /     / / / / / /|_/ / ")
    print("/ /_/ / ___/ // /____ / /_/ / / /  / /  ")
    print("\____(_)____(_)____(_)_____(_)_/  /_/   ")
    print("\n  Owen's Super Cool Disk Manager")
    print("          Ver. {}".format(ver))

def start(threeBit, sixBit, no):

    global ogPath
    #Super cool banner
    banner()
    #Simple ping test
    ping(ip)
    #Checking user installs
    insts(threeBit, sixBit, no)
    print("Final setup stuff...")
    print("Startup Complete!")
    time.sleep(3)
    return threeBit, sixBit

def menu(name, username, purpose, sixBit, threeBit, ip, yes, no, drive, port):

    global ogPath
    
    while True:

        clear()
        banner()
        print("\nWelcome to Owen's Super Cool Disk Manager!")
        print("The easy front-end for all of your SSHFS needs!")
        print("Please select a number:\n")
        print("[1]: Mount a SSHFS drive\n[2]: Un-Mount a SSHFS drive\n[3]: Test Connectivity\n[4]: Info\n[5]: Exit")
        
        try:
        
            menuInp = int(input("Enter a number:"))

        except:

            print("\nNaughty Naughty Naughty!\n")
            print("You tried to enter a letter, when I specificly said to enter a number!")
            print("Shame on you. You should be ashamed of yourself.")
            empty = input("\nPress ENTER(And only enter!) to continue...")
            continue
        
        if menuInp == 1:

            #Code for mounting drive here:
            mount(ip, username, port, drive)
            continue
        
        if menuInp == 2:

            #Code for unmounting drive here:
            umount(drive, ip, yes)
            continue
        
        if menuInp == 3:

            #Code for testing connectivity here:
            print("Are you sure you want to test connectivity?:")
            connecInp = input("\n(Y/N):")
            
            if connecInp in yes:

                clear()
                print("Starting conectivity test...")
                bug = True
                ping(ip, bug)
                continue

            else:

                continue

        if menuInp == 4:

            #Code for info here:
            info(name, username, purpose, sixBit, threeBit)
            continue

        if menuInp == 5:

            #Code for exiting:
            print("\nGoodbye!")
            time.sleep(1)
            exitTime(ogPath)
            
        else:

            print("\n'{}' is not a valid input :(".format(imenuInp))
            empty = input("\nPress enter to continue...")
            clear()
            continue

def mount(ip, username, port, drive):

    tempDrive = drive
    print("Enter drive letter, or leave the field blank to accept default(Z)\n")
    drive = input("Enter drive letter(Default is {}):".format(drive))
    if drive == '':

        drive = tempDrive

    print("\nWarning:\nYour password will be printed in clear text, on this very screen!")
    print("Please be wary of your surroundings, and don't let people look at your screen while typing this in.")
    print("You never know who might be watching!")
    passwd = input("\nPlease enter your password:")
    print('')
    formatString = "net use {}: \\\\sshfs\{}@{}!{}\.. {}".format(drive, username, ip, port, passwd)

    drivestat = os.system(formatString)

    if drivestat != 0:
        
        print("Failed to mount {} from host {} :(".format(drive, ip))
        print("Some debug info should be above")
        print("(Can you make anything of it?)")
        print("\nCommon Errors:")
        print("\n1. Access is denied: Password is incorrect/auth on serverside not working")
        print("2. The network name could not be found: Possible script bug/Server failure/Programs not installed correctly.")
        print("\nTry checking your password, testing connection, and re-installing programs.")
        print("Please contact Owen Cochell if you have any questions.")
        empty = input("Press enter to continue...")
        return

    else:

        print("Mounting Successfull!")
        print("You should now have access to the gamedev fileshare!")
        print("Open File Explorer and check out the 'My PC' tab!")
        empty = input("\nPress enter to continue...")
        return drive

def umount(drive, ip, yes):

    tempDrive = drive
    print("Please enter drive letter to remove, or leave blank for default({})".format(drive))
    drive = input("Enter drive letter(Default is {}):".format(drive))

    if drive == '':

        drive = tempDrive

    print("\nMake sure you don't have any files on the drive open, or this could lead to corruption")
    print("Just to be safe, you should probably close your File Explorer Windows(IF you have them open)")
    print("Are you sure you want to unmount drive {}?:".format(drive))
    mountInp = input("\n(Y/N):")
    if mountInp in yes:

        print("Unmounting drive {}...".format(drive))
        formatString = 'net use {}: /delete /Y'.format(drive)
        print('')
        umountDrive = os.system(formatString)

        if umountDrive != 0:

            print("Unable to remove drive {} :(")
            print("Some debug info should be above.\n(Can you make anything of it?)")
            print("Check the drive letter. You can tell what letter your drive is by checking under the 'My PC' tab.")
            print("Try closing ALL files and trying again, or restarting.")
            print("Please contact Owen Cochell for more info.")
            empty = input("\nPress enter to continue...")
            return

        else:

            print("Sucessfully un-mounted drive!")
            print("Check out the 'My PC' tab in file explorer!")
            print("To re-mount the drive, select 'Mount a SSHFS drive' from the main menu!")
            empty = input("\nPress enter to continue...")
            return
    else:

        return
    
    return

def info(name, username, purpose, sixBit, threeBit):

    #Code for info
    clear()
    print("+========================================================================+")
    print("Owen's Super Cool Disk Manager(O.S.C.D.M) ver. {}".format(ver))
    print("O.S.C.D.M is a easy front end for configuring network drives over the SSHFS protocol.")
    print("This script uses NO propriatary features or services,")
    print("And instead relies on the SSHFS-Win and Win-FSP programs.")
    print("More info on these programs can be found here:")
    print("\nSSHFS-Win:\nhttps://github.com/billziss-gh/sshfs-win")
    print("\nWinFsp:\nhttps://github.com/billziss-gh/winfsp/tree/v1.3")
    print("(This script can also install these programs and configure them for you.)")
    print("\nSome info on you:")
    print("\nName: {}".format(name))
    if name not in ('read-only', 'genral-Access'):

        print("(Wow, a script that was compiled just for you? WOW! You must be important!")
        
    print("\nUsername: {}".format(username))
    print("\nInfo: {}".format(purpose))
    print("\nThis script was created by:")
    print("+==============================================================+")
    print("   ____                         ______           __         ____")
    print("  / __ \_      _____  ____     / ____/___  _____/ /_  ___  / / /")
    print(" / / / / | /| / / _ \/ __ \   / /   / __ \/ ___/ __ \/ _ \/ / / ")
    print("/ /_/ /| |/ |/ /  __/ / / /  / /___/ /_/ / /__/ / / /  __/ / /  ")
    print("\____/ |__/|__/\___/_/ /_/   \____/\____/\___/_/ /_/\___/_/_/   ")
    print("+==============================================================+")
    x = input("Press enter to continue...")
    return

start(threeBit, sixBit, no)
menu(name, username, purpose, sixBit, threeBit, ip, yes, no, drive, port)




          
