import os

cmd = "pip install stdiomask"

try:
    import stdiomask
except:
    os.system(cmd)
#While loop line 13 to line 30 to be implemented at a later time

max = 5
used = 0
usedAll = False #Has the user used all login attempts
loggedIn = False #Is the user logged inggggg
rfl = False #Ready For Login

pswdReg = ""
pswdConf = ""
usr = ""
pswd = ""

print("\n___Python_Basic_Login___\n")

usrNReg = input("Register username:\t") #UserNameRegister
pswdReg = stdiomask.getpass(prompt = "Register password:\t", mask = "*") #passwordRegister
pswdConf = stdiomask.getpass(prompt = "Confirm password:\t", mask = "*") #passwordConfirm

if len(usrNReg) < 8:
	print("Username must contain at least 6 digits")

if len(pswdReg) < 8 or len(pswdConf) < 8:
    print("\nPassword must contain at least 8 digits\n")
    exit()

if pswdReg != pswdConf:
    print("\nPasswords does'nt mach, try again!\n")
else:
    print("\nLOGIN\n")
    rfl = True

if rfl == True:
    while used < max and not usedAll and not loggedIn:
        usr = input("Username: ")
        pswd = stdiomask.getpass(prompt = "Password: ", mask = "*")
        used += 1
        if usr == usrNReg and pswd == pswdReg:
            loggedIn = True
        else:
            print("\nLogin credentials not correct, try again!\n")
        if used == max:
            usedAll = True

if loggedIn:
    print(f"\n{usrNReg}, you succesfully logged in!")
    ch1 = int(input("Would you like to see username and password?\n1. Yes\n2. No\n>>> "))
    if ch1 == 1:
        print(f"Username:\t{usrNReg}\nPassword:\t{pswdReg}")
if usedAll:
    print(f"You have used all {max} attempts")
