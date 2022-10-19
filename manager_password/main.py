from cryptography.fernet import Fernet

'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key


key=load_key()   
fer=Fernet(key)




def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input('nome da conta: ')
    pwd = input('password: ')

    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Voce gostaria de adicionar uma nova senha ou visualizar as existentes(view,add), prescione q para sair: ")
    if mode =="q":
        break
    if mode=="view":
        view()
    if mode=="add":
        add()
    else:
        print("Invalid mode")
        continue