import hashlib
import getpass

def enkripsi_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password 

def periksa_kekuatan_password(password):
    if len(password) < 8:
        return False
        return True

def simpan_password(username,password):
    hashed_password = enkripsi_password(password)

def verifikasi_password(username,password):
    hashed_password = ''
    input_password = enkripsi_password(password)

    if input_password == hashed_password: 
       return True
    else:
        return False
        
#contoh Penguna

username = "MeianaSI23-A"
password = "231031003"

from getpass import getpass
uname = input("Enter a user name: ")
uname = uname.strip()
if uname!=username:
    print("Username pengguna salah. Selamat tinggal.") 
else:
    pword=input("Enter your password: ")
    pword = pword.strip()
if pword == password:
    print("welcome to our world of python")
else:
    print("Sandi salah. akses ditolak")
