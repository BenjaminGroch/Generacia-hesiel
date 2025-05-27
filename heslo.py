import random, string, subprocess

class Heslo:
    def __init__(self):
      #Cyklus na kontrolu ci uzivatel zadal spravny datovy typ ako dlzku hesla
        while True:
            try:                                                         #Uzivatel zada dlzku
                dlzka = int(input("zadajte požadovanú dĺžku hesla: "))
                if type(dlzka) == int:                                   #Ak je dlzka dobra, cyklus sa rusi
                    break
            except ValueError:                                           #Ak je dlzka zla, nepusti ho dalej kym nezada dobru dlzku
                print("Dlzka hesla musi byt cislo!!!")                    
        
        s_znaky = str(input("Pokial chcete v hesle specialne znaky napiste 'ano': ")) #Uzivatel zadava ci chce specialne znaky v hesle
        cisla = str(input("Pokial chcete v hesle cisla napiste 'ano': "))             #Uzivatel zadava ci chce cisla v hesle

        heslo = ''                                                                    #Tvorba prazneho hesla
        
        #Tvorba hesla s dlzkou ktoru uzivatel zada
        for i in range (dlzka):
            heslo += string.ascii_letters[random.randint(0,51)]             #Heslo je tvorene nahodnymi znakmi z kniznice string
        
        #Pridavanie znakov do hesla (ak uzivatel chce)
        if s_znaky == 'ano': 
            for i in range (random.randint(1,(dlzka//2))):                                 #Max pocet znakov je polovica hesla (aby sa nestalo ze heslo budu same znaky)
                j = random.randint(0,dlzka)
                heslo = heslo[:j] + string.punctuation[random.randint(0,31)] + heslo[j+1:] #Na nahodne pozicie pridava nahodne znaky z kniznice string
        
        #Pridavanie cisiel do hesla (ak uzivatel chce)
        if cisla == 'ano':
            for i in range (random.randint(1,(dlzka//2))):                                 #Max pocet cisel je polovica hesla (aby sa nestalo ze heslo budu same cisla)
                j = random.randint(0,dlzka)
                heslo = heslo[:j] + string.digits[random.randint(0,9)] + heslo[j+1:]       #Na nahodne pozicie pridava nahodne cisla z kniznice string
        
        #Vypis hesla do cli
        print(heslo)
        
        #Ukladanie hesla do txt suboru
        with open("hesla.txt","a") as f:
            f.write(heslo + "\n")
        
        #Ukladanie hesla do clipboardu
        def copy2clip(txt):
            cmd='echo '+txt.strip()+'|clip'
            return subprocess.check_call(cmd, shell=True)
        
        copy2clip(heslo)

h1 = Heslo()
