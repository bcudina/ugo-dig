
from tkinter import *
import sys
import datetime

root = Tk() 
import colorama
from colorama import Fore, Back, Style

colorama.init()

siva = (224,224,224)
red = (255,0,0)

                                    #tkinter definiranje prozora

root.geometry("700x400+50+50")                  #velicina prozora i definiranje mjesta na kojem se prozor otvara
root.title("Bozidar Cudina")

#root.mainloop()

#---------------------------------------------------------------------------------------------------------------
#-----------------------DEFINICIJE------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
def izbornik():
    izbor=input("izbor >> ")                                              #unesi izbor
    print()
    while izbor!='i' and izbor!='inv' and izbor!='bo' and izbor!='pdv' and izbor!='dig' and izbor!='help' and izbor!='menu':
        izbor=input("izbor mora biti : inv | bo | pdv | dig | help | menu | >>> ")                 #vraca pitanje ponovno
        
    if izbor == 'inv':                                                          #izracunava inventuru boca
        while True:
            jedan()
                 
    elif izbor == 'bo':
        boce()                                                           #pretvara 0.7 litara u 1 litru
                    
            
    elif izbor == 'pdv':                                                        #racuna obrnuti PDV
        while True:
            pdv_obrnuti()
            
    elif izbor == 'dig':                                                        #racuna obrnuti PDV
        while True:
            dig()
            
       
    elif izbor == 'menu':
        #print("     ..     ")
        #print("   (.)(.)   ")
        #print("    kraj    ")
        izbornik ()
        
        
        
    elif izbor == 'help':                                                        #racuna obrnuti PDV
        while True:
            help()    




    
def uvod():
    raspored = "{:<5}{:>20}{:>15}"
    raspored_2 = "{:<5}{:>25}{:>16}"
    raspored_3 = "{:<5}{:>18}{:>15}"
    vrijeme = datetime.datetime.now ()
    print(" "*39, vrijeme.strftime("%d %B %Y"))
    print("_"*55) 
    print (raspored.format(" inv - |INVENTURA|"," dig - |DIGITRON|", "help - |HELP|"))               #izbornik
    print (raspored_2.format(" bo  - |BOCE|", " xxx - |        |", " 00 - |NAZAD|"))
    print  (raspored_3.format(" pdv - |PDV obrnuti|", " xxx - |        |"," menu - |MENU|"))
    print("_"*55)  
    
    
def jedan():
    print (Back.YELLOW +'---------------- INVENTURA ----------------'+ Style.RESET_ALL)
    cijena_dozera=float(input("cijena dozera je >> "))
    if cijena_dozera==00:
        uvod()
        izbornik()
        
    pocetno_stanje=float(input("pocetno stanje je >> "))
    zavrsno_stanje=float(input("zavrsno stanje je >> "))
    potroseno= pocetno_stanje - zavrsno_stanje
    dozera = potroseno / 0.03
    cijena = cijena_dozera * dozera
    cijena_kratko = float("{:.2f}".format(cijena))
    print (Back.WHITE + Fore.BLACK + "iznos je ", cijena_kratko, "kn" + Style.RESET_ALL)
    print ("------")
    
def boce():
    print (Back.YELLOW +'------------------ BOCE ------------------'+ Style.RESET_ALL)
    ispis ="{:^17}|{:^10}|{:^10}|{:^15}"
    ispis_2 ="{:^9}|{:^8}|{:^10}|{:^8}"
    boca =[]
    while True:
        cijena=float(input("unesi cijenu boce od 0.7 litara bez PDVa: "))
        if cijena==00:
            uvod()
            izbornik()    
        kolicina=float(input("unesi kolicinu: "))
        cijena_1_litra=(cijena/7)*10                        
        cijena_kolicina=cijena_1_litra*kolicina
        
        short_cijena_1_litra=float("{:.2f}".format(cijena_1_litra))         #spusta float na dvije decimale
        short_cijena_kolicina=float("{:.2f}".format(cijena_kolicina))       #spusta float na dvije decimale
        print()
        print ("0.7l u 1l iznosi >>>", short_cijena_1_litra, "kn")
        print ("cijena * kolicina iznosi >>>",short_cijena_kolicina, "kn <<<" )
        print("_"*45)
        
        boca.append((cijena,   short_cijena_1_litra,   kolicina,   short_cijena_kolicina))
        print (ispis.format(Back.WHITE + Fore.BLACK + "  0.7  ", "  1  ", "kolicina", "cijena" + Style.RESET_ALL))
        print (ispis_2.format(Back.WHITE + Fore.BLACK + "litara ", "  litara  " , "", "" + Style.RESET_ALL))
        print("_"*45)
        
        for c in boca:
            print (c)
        print("_"*45)     
    
    

def pdv_obrnuti():
    print (Back.YELLOW +'---------------- PDV obrnuti ----------------'+ Style.RESET_ALL)
    cijena_sa_pdv=float(input("unesi cijenu sa PDV-om: "))
    if cijena_sa_pdv==00:
        uvod()
        izbornik()    
    osnovica = cijena_sa_pdv/1.25
    pdv = cijena_sa_pdv - osnovica
    print(Back.WHITE + Fore.BLACK + "osnovica = ", osnovica, ", a PDV =", pdv + Style.RESET_ALL)
    print("--------------------------------------") 

def help():
    print (Back.YELLOW +'---------------- HELP ----------------'+ Style.RESET_ALL)
    print ("INVENTURA")
    print ("U program se unosi cijena dozera pica koja se naplacuje gostu,")
    print ("pocetna kolicina stanja na sanku i krajnja zavrsna kolicina.")
    print ("Program daje kao izlaz novcanu vrijednost koju personal predaje")
    print ("za tu vrstu pica.")
    print ("--------------------------------------------------")
    print ("BOCE")
    print ("program uzima postojecu cijenu boce od 0.7 litara i preracunava")
    print ("koliko bi ta boca kostala da je od 1 litre. Cijena je bez PDV-a.")
    print ("U drugoj linije daje vrijednost tako preracunatih boca")
    print ("sa inventurnom kolicinom.")
    print ("--------------------------------------------------")
    print ("PDV obrnuti")
    print ("U program se unosi konacna ili krajnja /bruto/ cijena sa PDV-om.")
    print ("Kao izlaz dobije se pocetna cijena ili osnovica i iznos PDV-a od 25%.")
    print ("--------------------------------------------------")
    i=input("pretisni /00/ za izlaz : ")
    if i=="00":
        uvod()
        izbornik()
    else:
        print("Hvala sto ste upotrebljavali program")      
        
        
def dig ():
    raspored = "{:<5}{:>17}"
    raspored_2 = "{:<7}{:>23}"
    
    print (Back.YELLOW + Fore.BLACK + '-------- PRERACUNAVANJE MJERNIH JEDINICA --------' + Style.RESET_ALL)
    print ()
    print (raspored.format(" pre - |PRERACUNAVANJE|"," brz - |BRZINA|"))
    print (raspored_2.format(" xxx - |-----|"," 000 - |MENU|"))
   
    
    print("_"*50) 
    dig_izbor = input (' izbor >> ')
    
    if dig_izbor == 'menu':
        izbornik ()
    elif dig_izbor == 'pre':
        preracunavanje () 
    elif dig_izbor == 'brz':
        brzina ()
        
        
        
        
def preracunavanje ():
    iznos = float(input('...unesi brojcanu vrijednost >> '))
    if iznos == 00 :
        uvod ()
        izbornik ()
    
    velicina = input('...upisi zadanu velicina u: | km | m | dm | cm | mm | >>> ')
    while velicina!='km' and velicina!='m' and velicina!='dm' and velicina!='cm' and velicina!='mm':
        velicina = input('...zadana velicina MORA biti jedna od : | km | m | dm | cm | mm | >>> ')
    print ()
            
    if velicina == 'km':
        
        mm = iznos * 1000000
        cm = iznos * 100000
        dm = iznos * 10000
        m =  iznos * 1000
        
        print (Back.WHITE + Fore.RED + ' vrijednost', iznos, 'km iznosi  ' + Style.RESET_ALL)    
        print (Back.WHITE + Fore.BLACK + '|',mm, ' mm |', cm,' cm |', dm,' dm | ', m,' m |' + Style.RESET_ALL) 
        print ()
        doc = open ("preracunavanje_km.txt", "w+")
        doc.write ("kako je biti mali")
        doc.close()
        preracunavanje ()
    
               

    elif velicina == 'm':
        mm = iznos * 1000
        cm = iznos * 100
        dm = iznos * 10
        km = iznos / 1000
    
        print (Back.WHITE + Fore.RED + ' vrijednost', iznos, 'm iznosi  ' + Style.RESET_ALL)
        print (Back.WHITE + Fore.BLACK + '|',mm, 'mm |', cm,' cm |', dm,' dm |', km,' km |'+ Style.RESET_ALL) 
        print ()
        preracunavanje ()
    
    elif velicina == 'dm':
        mm = iznos * 100
        cm = iznos / 10
        m =  iznos / 1000
        km = iznos / 100000
    
        print (Back.WHITE + Fore.RED + ' vrijednost', iznos, 'dm iznosi  ' + Style.RESET_ALL)
        print (Back.WHITE + Fore.BLACK + '|', mm,' mm |', cm,' cm |', m,' m |', km,' km |'+ Style.RESET_ALL)
        print ()
        preracunavanje ()
        
    elif velicina == 'cm':
        mm = iznos * 10
        dm = iznos / 10
        m =  iznos / 100
        km = iznos / 10000
    
        print (Back.WHITE + Fore.RED + ' vrijednost', iznos, 'cm iznosi  ' + Style.RESET_ALL)
        print (Back.WHITE + Fore.BLACK + '|',mm, 'mm |', dm,' dm |', m,' m |', km,' km |'+ Style.RESET_ALL)
        print ()
        preracunavanje ()
        
    elif velicina == 'mm':
        cm = iznos / 10
        dm = iznos / 100
        m =  iznos / 1000
        km = iznos / 1000000
    
        print (Back.WHITE + Fore.RED + ' vrijednost', iznos, 'mm iznosi  ' + Style.RESET_ALL)
        print (Back.WHITE + Fore.BLACK + '|', cm,' cm |', dm,' dm |', m,' m |', km,' km |'+ Style.RESET_ALL)
        print ()
        preracunavanje ()
    
          
        

def brzina ():
    raspored = "{:<5}{:>29}"
    print (Back.YELLOW +'-------- PRERACUNAVANJE BRZINE --------'+ Style.RESET_ALL)
    print ()
    print (raspored.format(" 1 - |km/h ---> m/s|"," 2 - |m/s ---> km/h|"))
    print("_"*50) 
    dig_brzina = int(input('izbor: '))
    
    if dig_brzina == 1:
        km_h = float(input('unesi vrijednost u km/h '))
        m_s = km_h *3.6
        print(Back.WHITE + Fore.BLACK + 'brzina od ',km_h, 'iznosi ', m_s,' m/s'+ Style.RESET_ALL)
        print (' ')
        brzina ()
    elif dig_brzina == 2:
        m_s = float(input('unesi vrijednost m/s '))
        km_h = m_s / 3.6
        print (Back.WHITE + Fore.BLACK + 'brzina od ', m_s, 'iznosi ', km_h, 'km/h'+ Style.RESET_ALL)
        print (' ')
        brzina ()
        
                   
                    
    
          

        


    

# POCETAK PROGRAMA ------------------------------------------------------

uvod()

izbornik()


 


