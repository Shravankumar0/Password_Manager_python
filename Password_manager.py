import random
import string

passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars =string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password


while True:
     print("----password manager----")
     print("1. Save password") 
     print("2. View password")
     print("3. Generate password")
     print("4. Exit")
     
     choice = input("Enter your choice : ")
     if choice == "1":
         site = input("Enter website : ")
         pwd = input("Enter password : ")
         passwords[site] = pwd
         with open("passwords.txt","a") as file:
             file.write(f"{site}:{pwd}\n")
         
         print("saved!")
     elif choice == "2":
         if not passwords:
             print("No data")
         else:
             for site, pwd in passwords.items():
                 print(site, ":" , pwd)
     elif choice == "3":
         print("Genereted password : " , generate_password())
         
     elif choice == "4":
         print("by by ...!")
         break
     
     else:
         print("In-Valid choice....! ")                    
                             