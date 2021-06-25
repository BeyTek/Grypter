from cryptosteganography import CryptoSteganography
import time
import datetime 
import glob, os
from secure_delete import secure_delete
from colorit import *
import getpass
import stdiomask
import random
from PIL import Image
import numpy as np
import shutil
import subprocess
import sys

secure_delete.secure_random_seed_init()
init_colorit()
TodayDate = datetime.datetime.today().strftime ('%d-%b-%Y')
home =os.environ["HOMEPATH"]

directory = "Grypter"
parent_dir = home +"/Desktop"
path = os.path.join(parent_dir, directory) 
try:
    os.mkdir(path)
except OSError:
    print ("directory %s already exist" % path)
else:
    print ("Successfully created the directory %s " % path)

 

def generate_random_image(width=58, height=58):
    data=np.random.randint(low=0,high=256,size=128*128*3, dtype=np.uint8)
    data=data.reshape(128,128,3)
    Image.fromarray(data,'RGB').save("base.jpg")



print(color("   _____                  _            ", Colors.green))
print(color("  / ____|                | |           ", Colors.green))
print(color(" | |  __ _ __ _   _ _ __ | |_ ___ _ __ ", Colors.green))
print(color(" | | |_ | '__| | | | '_ \| __/ _ \ '__|", Colors.green))
print(color(" | |__| | |  | |_| | |_) | ||  __/ |  ", Colors.green))
print(color("  \_____|_|   \__, | .__/ \__\___|_|  ", Colors.green))
print(color("               __/ | |                ", Colors.green))
print(color("              |___/|_|                 ", Colors.green))


def  menu():
    
    print(color("[1]Encrypt",Colors.red))
    print(color("[2]Decrypt",Colors.blue))
    print(color("[3]Clean & Quit",Colors.yellow))

menu()
option = int(input("Choose A Number: "))

while option != 0:
        if option == 1:
            generate_random_image()
            mdp_sec = stdiomask.getpass(prompt='password: ', mask='*')
            msg_secret = input("\nmessage: ")
            crypto_steganography = CryptoSteganography(mdp_sec)
            crypto_steganography.hide('base.jpg',str(TodayDate +'.png'), msg_secret)    
            src1_dir = "C:/Grypter/"
            dst1_dir = home+"/Desktop/Grypter/"
            for pngfile in glob.iglob(os.path.join(src1_dir, "*.png")):
                shutil.copy(pngfile, dst1_dir) 
            time.sleep(2)
            print(TodayDate,"is now encrypted on your Desktop")
            secure_delete.secure_delete('base.jpg')
            for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
            time.sleep(2)
            secure_delete.secure_delete('file.png')
            time.sleep(2)
            print("Enjoy!\n")
            print(color("www.dnz.re",Colors.blue))
            time.sleep(5)
            quit()

   

        if option == 2:
            print(color("Place The encrypted image in the Grypter folder, on the Desktop",Colors.orange))
            for remaining in range(20, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write(color("{:2d} seconds remaining to place image in the folder.".format(remaining),Colors.green)) 
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\r\nComplete!            \n")
            src2_dir = home+"/Desktop/Grypter/"
            dst2_dir = "C:/Grypter/"
            for pngfile in glob.iglob(os.path.join(src2_dir, "*.png")):
                shutil.copy(pngfile, dst2_dir) 
            time.sleep(2)
            for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
            time.sleep(2) 
            secret = stdiomask.getpass(prompt='Password: ', mask='*')
            crypto_steganography = CryptoSteganography(secret)
            secret = crypto_steganography.retrieve('file.png')
            print("SECRET MESSAGE IS :","\n\n",color(secret,Colors.green))
            print(color("\nMESSAGE AUTO-DELETE AFTER 30 SECONDS" ,Colors.red))
            secure_delete.secure_delete(home + "\\Desktop\\Grypter")
            secure_delete.secure_delete('file.png')
            time.sleep(30)
            print("Enjoy!\n")
            print(color("www.dnz.re",Colors.blue))
            time.sleep(5)
            quit()

        if option == 3:
            secure_delete.secure_delete('file.png')
            secure_delete.secure_delete(home + "\\Desktop\\Grypter")
            os.system('CLS')
            time.sleep(3)
            quit()
