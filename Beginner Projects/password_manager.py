#Type 'pip install cryptography' in the Terminal to encrypt passwords.
from cryptography.fernet import Fernet
# cryptography.fernet allows us to encrypt text. May need to restart IDE or Code Editor if it isn't recognised straight away.


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""
#This functions going to create and open a file called "key.key" in "wb" mode (write in bite) as key file.
#Then we write in the Fernet key.

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#master_pwd = input("What is the Master Password? ")
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)
#encode will take my string and turn it into bytes
#you would add the master_pwd in conjuctuon with fernet on: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWp3MmExMzFFR0NfSWFCSWxrX3MtR2ZKdE42UXxBQ3Jtc0tuRmEySWowY01PbjBQVHBoTWh2dnpia3BzYXdGWWRJWHhxYWQ4RU1iSmZaZUtXSllrVEhQMDUwVkdLd0thU2tETHdicDYxc1l2cXFWemd2bDlCSUJacWJoX005OWo0MkNYNG1Eb2VHZEl0VENDNU42SQ&q=https%3A%2F%2Fcryptography.io%2Fen%2Flatest%2Ffernet%2F&v=DLn3jOsNRVE

def view():
    with open('pwdman.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
            
# f.readlines does what it says, reads lines.
# .split will split the strings by searching for my choice of character ("|") to seperate them.      

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('pwdman.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# 'with' is used to open and automatically close files
# 'passwords.txt' is the name of the file. 'a' is the mode.

"""The main modes in python are 'a', 'r', 'w'.
'w' overwrites files mode.
'r' read only mode
'a' adds something to an existing file. Or creates a new file if it doesn't exist"""

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue