#json: Provides json functions
#os: provides os funcions
#cryptography: prvoides encryption/decryption
#pyperclip: copy to clipboard function (SOON)

#prereq: passwd.json, UI.json, and key.key exists
'''
passwd.json structure 
"website": "xxxx",
"username": "xxxx",
"password": "xxxx"
'''
import json, os, cryptography
from cryptography.fernet import Fernet

passwd_file = 'passwd.json'
UI_file = '' #fill in later
key_file = 'key.key'
#key = in gen_key()

#for later emoji
#\U0001F975

#ONLY RUN ONCE, IF RUN AGAIN ENCRYTED FILE CANNOT BE DECRYPTED
def gen_key():
    return Fernet.generate_key()

def obfuscate_key():
    with open(key_file, 'rb') as k:
        key = k.read()
    
    '''XOR CIPHER IT '''
'''ADD ANOTHER FUNCITON
def deobfuscate_key()
that does the opposite'''

def encrypt_file():
    print("Encrypting passwd.json")
    #opening key.key
    with open(key_file,'rb') as k:
        key = k.read()

    #opening passwd.json
    with open(passwd_file, 'rb') as f:
        pswd = f.read()

    #encrypts
    fernet = Fernet(key)
    encrypted = fernet.encrypt(pswd)

    #overwrites passwd_file with the new information
    with open(passwd_file,'wb') as e:
        e.write(encrypted)

def decrypt_file():
    print("Decrypting passwd.json")

    with open(key_file, 'rb') as k:
        key = k.read()

    with open(passwd_file, 'rb') as f:
        pswd = f.read()
    
    #decrypts
    fernet = Fernet(key)
    decrypts = fernet.decrypt(pswd)

    #overwrites passwd_file with the new information
    with open(passwd_file,'wb') as d:
        d.write(decrypts)


###################
#       MAIN      #
###################
#First Run Instructions

#Checking prereq
#creates/check if password.json exists
if (os.path.exists(passwd_file) == False):
    print("Creating passwd.json...")
    f = open(passwd_file,'w')

    #creates test json information
    json.dump({
        "website": "example.com",
        "username": "jamontypes",
        "password": "xoaddd"
    }, f)

    f.close()        
    
#creates/check if a key was generated
if (os.path.exists(key_file) == False):
    print ("Generating Key...")
    f = open(key_file, "wb")
    f.write(gen_key())
    f.close() 

''' For later 
if (os.path.exists(UI_file) == False):
    print("Creating neccessary file...")
    f = open(UI_file,'w')
    f.close()
'''

#Logging in
#decrypts passwd.json
decrypt_file()



#Logging Out 
#encrypts passwd.json
encrypt_file()

