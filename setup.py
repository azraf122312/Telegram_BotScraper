import os
import sys
import time
import requests
import configparser
import pandas as pd
import sys


def requirements():
    def csv_lib():
        banner()
        print("Please wait a bit")
        os.system("""
			pip3 install numpy pandas
			python3 -m pip install cython nympy pandas""")

    input_csv = input('Do You Want to enable csv merge (y/n) : ')
    if input_csv == "y":
        csv_lib()
    else:
        pass

    print("Intalling ........")
    os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data """)

    banner()
    print("requirements installed")


def config_setup():
    banner()
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    xid = input(gr + "[+] enter api ID : " + re)
    cpass.set('cred', 'id', xid)
    xhash = input(gr + "[+] enter hash ID : " + re)
    cpass.set('cred', 'hash', xhash)
    xphone = input(gr + "[+] enter phone number : " + re)
    cpass.set('cred', 'phone', xphone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print(gr + "[+] setup complete !")


def merge_csv():
    import pandas as pd
    import sys
    banner()
    file1 = pd.read_csv(sys.argv[2])
    file2 = pd.read_csv(sys.argv[3])
    print(' merging ' + sys.argv[2] + ' & ' + sys.argv[3] + ' ...')
    merge = file1.merge(file2, on='username')
    merge.to_csv("output.csv", index=False)
    print(' saved !!!!! file as "output.csv"\n')
