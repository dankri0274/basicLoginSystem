import os
import sys

cmd = "pip install stdiomask"
cmd2 = "pip install termcolor"

try:
    import stdiomask
    from termcolor import colored
except:
    os.system(cmd)
    os.system(cmd2)
    
#While loop line 13 to line 30 to be implemented at a later time

max = 5
used = 0
usedAll = False #Has the user used all login attempts
loggedIn = False #Is the user logged in
rfl = False #Ready For Login

pswdReg = ""
pswdConf = ""
usr = ""
pswd = ""

print("\n___Python_Basic_Login___\n")

usrNReg = input("Register username:\t") #UserNameRegister
pswdReg = stdiomask.getpass(prompt = "Register password:\t", mask = "*") #passwordRegister
pswdConf = stdiomask.getpass(prompt = "Confirm password:\t", mask = "*") #passwordConfirm

if len(usrNReg) < 6:
	print(colored("Username must contain at least 6 digits", "red"))

if len(pswdReg) < 8 or len(pswdConf) < 8:
    print(colored("\nPassword must contain at least 8 digits\n", "red"))
    exit()

if pswdReg != pswdConf:
    print(colored("\nPasswords does not mach, try again!\n", "red"))
else:
    print(colored("\nLOGIN\n", "green"))
    rfl = True

if rfl == True:
    while used < max and not usedAll and not loggedIn:
        usr = input("Username: ")
        pswd = stdiomask.getpass(prompt = "Password: ", mask = "*")
        used += 1
        if usr == usrNReg and pswd == pswdReg:
            loggedIn = True
        else:
            print(colored("\nLogin credentials not correct, try again!\n", "red"))
        if used == max:
            usedAll = True

if loggedIn:
    print(colored(f"\n{usrNReg}, you succesfully logged in!", "green"))
    ch1 = int(input("Would you like to see username and password?\n1. Yes\n2. No\n>>> "))
    if ch1 == 1:
        print(f"Username:\t{usrNReg}\nPassword:\t{pswdReg}")
if usedAll:
    print(f"You have used all {max} attempts")
