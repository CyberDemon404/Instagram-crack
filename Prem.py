import os

# Ngapain Bang?
# Kalo Mau Recode Izin Dulu Boss:v
def ___rozhak___():
    try:
        ___file = open('rozhak','r').read()
    except (IOError):
        print("\x1b[1;93m*! Silahkan Tunggu 1-3 Menit...")
        os.system('gcc `python2-config --cflags --ldflags` __pycache__/main.c -o rozhak')
        os.system("./rozhak")
    else:
        os.system('./rozhak')

___rozhak___()
