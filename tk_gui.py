from tkinter import *

def prosta_funkcja():
    print("Prosta funkcja.")

root=Tk()
root.geometry('800x700')
root.title('Map Book.Sg')

#ramki do porządkowania struktury
ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_pokaz_szczegoly=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_pokaz_szczegoly.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0)


#ramka lista użytkowników

label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow,text='Lista obiektów')
listbox_lista_uzytkownikow=Listbox(ramka_lista_uzytkownikow,width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow,text='pokaż szczegoly')
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow,text='edytuj')
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text='usuń')

ramka_lista_uzytkownikow.grid(row=0, column=0)
listbox_lista_uzytkownikow.grid(row=1, column=0,columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_uzytkownika.grid(row=2, column=1)
button_usun_uzytkownika.grid(row=2, column=2)

# ramka formularz

label_formularz=Label(ramka_formularz,text='formularz edycji i dodawania')
label_imie=Label(ramka_formularz,text='imie')
label_nazwisko=Label(ramka_formularz,text='nazwisko')
label_posty=Label(ramka_formularz,text='posty')
label_miejsowosc=Label(ramka_formularz,text='miejsowosc')
entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)






label_formularz.grid(row=0, column=0,columnspan=2)
label_imie.grid(row=1, column=0,sticky=W)
label_nazwisko.grid(row=2, column=0,sticky=W)
label_posty.grid(row=3, column=0,sticky=W)
label_miejsowosc.grid(row=4, column=0,sticky=W)
button_usun_uzytkownika.grid(row=5, column=0,sticky=W)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
entry_miejscowosc.grid(row=4, column=1)




#ramka_pokaz_szczegoly
label_opis_uzytkownika=Label(ramka_mapa,text='szczególy uzytkownika')
label_imie_szczegoly=Label()


root.mainloop()