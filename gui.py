import klassy
import Main
import tkinter as tk


#wyglad okna
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.okno()
        self.dane_form()
        self.bindy()
        self.entry1.focus_set()


    #metoda :glowne okno
    def okno(self):
        #tytul
        self.title('System J.sgp')

        #kolor okna
        self.config(bg='black')

        #wymiary okna
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        centry_x = int(screen_width / 2 - window_width / 2)
        centry_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{centry_x}+{centry_y}')

        #--- tutaj wszytskie potrzbne ramki-----

        #ramka na strone 1 logowanie
        self.Frame_logowanie = tk.Frame(self, bg='black')
        self.Frame_logowanie.place(relx=0, rely=0, relwidth=1, relheight=1)

        #ramka na Strona 2 zalogowany
        self.Frame_zalogowany = tk.Frame(self, bg='black')
        self.Frame_zalogowany.place(relx=0, rely=0, relwidth=1, relheight=1)

        #ramka na Strone 3 dodaj formakte
        self.Frame_dodaj = tk.Frame(self, bg='black')
        self.Frame_dodaj.place(relx=0, rely=0, relwidth=1, relheight=1)

        #ramka na Strone 33 usun formatke
        self.Frame_usun = tk.Frame(self, bg='black')
        self.Frame_usun.place(relx=0, rely=0, relwidth=1, relheight=1)

        #ramka na Strone 333 pokaz lokalizacje
        self.Frame_pokaz=tk.Frame(self,bg='black')
        self.Frame_pokaz.place(relx=0, rely=0, relwidth=1, relheight=1)

        #ramka 2.1 zalogowany admin
        self.Frame_zalogowany_admin=tk.Frame(self, bg='black')
        self.Frame_zalogowany_admin.place(relx=0, rely=0, relwidth=1, relheight=1)





        #--------------------------------- ramka logowania -----------------------------------
        # login:
        self.label1 = tk.Label(self.Frame_logowanie, text='Login:', bg='black', fg='green',
                               font=('Arial', 16, 'normal'))
        self.label1.place(x=238, y=165)
        #----miejsce gdzie wpisuje login---
        self.entry1 = tk.Entry(self.Frame_logowanie, bg='black', fg='green', width=12, insertbackground='green', bd=0,
                               highlightthickness=0, font=('Arial', 16, 'normal'))
        self.entry1.place(x=306, y=167)
        #---kreska pod  loginem----
        self.kreska1 = tk.Frame(self.Frame_logowanie, bg='green', width=146, height=2)
        self.kreska1.place(x=306, y=190)

        #haslo

        #----napis---
        self.label2 = tk.Label(self.Frame_logowanie, text='Password:', bg='black', fg='green',
                               font=('Arial', 16, 'normal'))
        self.label2.place(x=238, y=202)

        #----miejsce gdzie wpisuje haslo----
        self.entry2 = tk.Entry(self.Frame_logowanie, bg='black', fg='green', width=9, insertbackground='green', bd=0,
                               highlightthickness=0, font=('Arial', 16, 'normal'))
        self.entry2.place(x=347, y=204)

        #----krestka pod haslem----
        self.kreska2 = tk.Frame(self.Frame_logowanie, bg='green', width=105, height=2)
        self.kreska2.place(x=347, y=227)

        #------komunikat jesli haslo jest zle ---
        self.zle_haslo = tk.Label(self.Frame_logowanie, text='', bg='black',
                                  fg='red',font=('Arial', 11, 'normal'))
        self.zle_haslo.place(x=230, y=235)






        #-------------------------------------ramka zalogowany --------------------------------
        #--- okno welcom ---
        self.welcom = tk.Label(self.Frame_zalogowany, text='Witamy w systemie "Jebac SGP"', bg='black', fg='green',
                               font=('Arial', 20, 'normal'))
        self.co_chcesz = tk.Label(self.Frame_zalogowany, text='Wybierz co chcesz zrobic:', bg='black', fg='green',
                                  font=('Arial', 20, 'normal'))






        #-------------------------------------ramke dodaj_form-----------------------------------------
        #komunikat
        self.kom1=tk.Label(self.Frame_dodaj,text='Podaj dane formatki ktora chcesz dodac:',bg='black', fg='green',
                           font=('Arial', 30, 'normal'))
        self.linia1=tk.Frame(self.Frame_dodaj,bg='green',width=111111, height=4)
        # Kod formatki
        self.label3 = tk.Label(self.Frame_dodaj, text='Kod formatki:', bg='black', fg='green',
                               font=('Arial', 20, 'normal'))
        self.entry3 = tk.Entry(self.Frame_dodaj, bg='black', fg='green', width=4, insertbackground='green', bd=0,
                               highlightthickness=0,
                               font=('Arial', 16, 'normal'))
        self.kreska3 = tk.Frame(self.Frame_dodaj, bg='green', width=50, height=2)

        #lokalizacja Formatki
        self.label4 = tk.Label(self.Frame_dodaj, text='Lokalizacja:', bg='black', fg='green',
                               font=('Arial', 20, 'normal'))
        self.entry4 = tk.Entry(self.Frame_dodaj, bg='black', fg='green', width=7, insertbackground='green', bd=0,
                               highlightthickness=0,
                               font=('Arial', 16, 'normal'))
        self.kreska4 = tk.Frame(self.Frame_dodaj, bg='green', width=77, height=2)

        # ilosc Formatki
        self.label5 = tk.Label(self.Frame_dodaj, text='ilosc pojemnikow:', bg='black', fg='green',
                               font=('Arial', 20, 'normal'))
        self.entry5 = tk.Entry(self.Frame_dodaj, bg='black', fg='green', width=3, insertbackground='green', bd=0,
                               highlightthickness=0,
                               font=('Arial', 16, 'normal'))
        self.kreska5 = tk.Frame(self.Frame_dodaj, bg='green', width=40, height=2)

        #pusty tekst do ktorego dodajemy komunkaty z Klass
        self.pusty_tekst = tk.Label(self.Frame_dodaj, text='', bg='black', fg='green', font=('Arial', 20, 'normal'))
        self.pusty_tekst.place(relx=0.5, rely=0.5, anchor='center')





        #----------------------- ramka usun_form ----------------
        #komunikat
        self.kom11 = tk.Label(self.Frame_usun, text='Podaj dane formatki ktora chcesz usunac:', bg='black', fg='green',
                             font=('Arial', 30, 'normal'))
        self.linia11 = tk.Frame(self.Frame_usun, bg='green', width=111111, height=4)


        # Kod formatki
        self.label33 = tk.Label(self.Frame_usun, text='Kod formatki:', bg='black', fg='green',
                                font=('Arial', 20, 'normal'))
        self.entry33 = tk.Entry(self.Frame_usun, bg='black', fg='green', width=4, insertbackground='green', bd=0,
                                highlightthickness=0,
                                font=('Arial', 16, 'normal'))
        self.kreska33 = tk.Frame(self.Frame_usun, bg='green', width=50, height=2)


        # lokalizacja Formatki
        self.label44 = tk.Label(self.Frame_usun, text='Lokalizacja:', bg='black', fg='green',
                                font=('Arial', 20, 'normal'))
        self.entry44 = tk.Entry(self.Frame_usun, bg='black', fg='green', width=7, insertbackground='green', bd=0,
                                highlightthickness=0,
                                font=('Arial', 16, 'normal'))
        self.kreska44 = tk.Frame(self.Frame_usun, bg='green', width=77, height=2)


        # ilosc Formatki
        self.label55 = tk.Label(self.Frame_usun, text='ilosc pojemnikow:', bg='black', fg='green',
                                font=('Arial', 20, 'normal'))
        self.entry55 = tk.Entry(self.Frame_usun, bg='black', fg='green', width=3, insertbackground='green', bd=0,
                                highlightthickness=0,
                                font=('Arial', 16, 'normal'))
        self.kreska55 = tk.Frame(self.Frame_usun, bg='green', width=40, height=2)


        # pusty tekst do ktorego dodajemy komunkaty z Klass
        self.pusty_tekst1 = tk.Label(self.Frame_usun, text='', bg='black', fg='green', font=('Arial', 20, 'normal'))
        self.pusty_tekst1.place(relx=0.5, rely=0.5, anchor='center')


        #---------------------------ramka pokaz lokalizacje -------------------------------------------------------
        #komunikat
        self.kom111=tk.Label(self.Frame_pokaz,text='Wpisz kod aby zobaczyc jego lokalizacje:', bg='black', fg='green',
                             font=('Arial', 30, 'normal'))
        self.linia111=tk.Frame(self.Frame_pokaz, bg='green', width=111111111, height=4)

        #kod formatki
        self.label333=tk.Label(self.Frame_pokaz,text='Podaj kod formatki :', bg='black', fg='green',
                               font=('Arial', 20, 'normal'))
        self.entry333=tk.Entry(self.Frame_pokaz,bg='black', fg='green', width=4, insertbackground='green', bd=0,
                                highlightthickness=0,font=('Arial', 20, 'normal'))
        self.kreska333=tk.Frame(self.Frame_pokaz, bg='green', width=60, height=2)

        #komunikat
        self.pusty_tekst11=tk.Label(self.Frame_pokaz,text='', bg='black', fg='green', font=('Arial', 20, 'normal'))
        self.pusty_tekst11.place(relx=0.5, rely=0.5, anchor='center')



        #ramka zalogowany admin
        self.label6=tk.Label(self.Frame_zalogowany_admin,text='Witam Admina Lotnik !!!!!!!',bg='black', fg='green',font=('Arial', 40, 'normal'))
        self.kreska6=tk.Frame(self.Frame_zalogowany_admin,bg='green', width=11111, height=6)

        self.tekst6=tk.Label(self.Frame_zalogowany_admin,text='Wcisnij czerwony guzik aby calkowicie wyczyscic magazyn'
                             ,bg='black',fg='yellow',font=('Arial', 20, 'normal'))
        self.pusty_tekst6=tk.Label(self.Frame_zalogowany_admin,text='',bg='black',fg='green',font=('Arial', 20, 'normal'))










        #---------   PRZYCISKI     --------

        # Dodaj formatke
        self.dodaj_form = tk.Button(self.Frame_zalogowany, text='Dodac Formatke          ', bg='yellow', fg='black',
                                    font=('Arial', 15, 'normal'),
                                    command=self.pokaz_dodaj)

        # usun formatke
        self.usun_form = tk.Button(self.Frame_zalogowany, text='Usunac Formatke             ', bg='yellow', fg='black',
                                   font=('Arial', 15, 'normal'),
                                   command=self.pokaz_usun)

        # sprawdzenie lokalizacji
        self.show_lok = tk.Button(self.Frame_zalogowany, text='Zobaczyc lokalizacje formatki', bg='yellow', fg='black',
                                  font=('Arial', 15, 'normal'),
                                  command=self.pokaz_pokaz)



        #przyciski do czyszczenia calego magazynu dla admina
        self.admin=tk.Button(self.Frame_zalogowany_admin,text='Wyczysci caly magazyn',bg='red',fg='white',
                             font=('Arial', 40, 'normal'),
                             command=self.wyczysc_magazyn)


    # metoda : dane formatki
    def dane_form(self):

        #tutaj do dodawanie formatek
        #komunikat
        self.kom1.place(x=10, y=30)
        self.linia1.place(x=0,y=87)


        # Kod formatki
        self.label3.place(x=10, y=110)
        self.entry3.place(x=178, y=117)
        self.kreska3.place(x=178 , y=140)

        #lokalizacja formatki
        self.label4.place(x=10, y=150)
        self.entry4.place(x=161, y=157)
        self.kreska4.place(x=161, y=180)

        # ilosc Formatki
        self.label5.place(x=10, y=190)
        self.entry5.place(x=231, y=197)
        self.kreska5.place(x=231, y=220)



        #tutaj do usuwania formatek
        #komunikat
        self.kom11.place(x=10,y=30)
        self.linia11.place(x=0,y=87)
        # Kod formatki
        self.label33.place(x=10, y=110)
        self.entry33.place(x=178, y=117)
        self.kreska33.place(x=178, y=140)

        #lokalizacje formatki
        self.label44.place(x=10, y=150)
        self.entry44.place(x=161, y=157)
        self.kreska44.place(x=161, y=180)

        # ilosc Formatki
        self.label55.place(x=10, y=190)
        self.entry55.place(x=231, y=197)
        self.kreska55.place(x=231, y=220)


        #tutaj do pokazywania lokalizacji
        #komunikat
        self.kom111.place(x=10,y=30)
        self.linia111.place(x=0,y=87)

        #kod formatki
        self.label333.place(x=100,y=111)
        self.entry333.place(x=348, y=113)
        self.kreska333.place(x=348, y=145)



        self.Frame_logowanie.tkraise()
        self.entry1.focus_set()
        self.Frame_current = 'logowanie'

    # metoda pomocnicza do przycisku dodaj_form
    def pokaz_dodaj(self):
        self.czyszczenie_okna()
        self.dane_form()
        self.Frame_dodaj.tkraise()
        self.entry3.focus_set()
        self.Frame_current = 'dodaj'

    # metoda pomocnicza do przycisku usun_form
    def pokaz_usun(self):
        self.czyszczenie_okna()
        self.dane_form()
        self.Frame_usun.tkraise()
        self.entry33.focus_set()
        self.Frame_current = 'usun'

    def pokaz_pokaz(self):
        self.czyszczenie_okna()
        self.dane_form()
        self.Frame_pokaz.tkraise()
        self.entry333.focus_set()
        self.Frame_current = 'pokaz'
    def wyczysc_magazyn(self):
        self.pusty_tekst6.config(text='Wyczyszczono caly magazyn prawidlowo')
        self.magazyn=klassy.MagazynP()
        self.magazyn.z_plik()
        self.magazyn.wyczysc_magazyn()
        self.magazyn.to_plik()



    #metoda do czyszczenie calego okna
    def czyszczenie_okna(self):
        self.config(bg='black')
        self.label1.place_forget()
        self.label2.place_forget()
        self.entry1.place_forget()
        self.entry2.place_forget()
        self.kreska1.place_forget()
        self.kreska2.place_forget()
        self.zle_haslo.place_forget()
        self.welcom.place_forget()
        self.co_chcesz.place_forget()
        self.dodaj_form.place_forget()
        self.usun_form.place_forget()
        self.show_lok.place_forget()

    # metoda : kiedy sie zalogujemy
    def zalogowano(self, event):
        self.login = self.entry1.get()
        self.haslo = self.entry2.get()

        # zalogowany
        if self.login == 'plkmaga2' and self.haslo == 'plkmag2':
            self.Frame_zalogowany.tkraise()
            self.Frame_current = 'zalogowano'
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')


            self.czyszczenie_okna()
            self.welcom.place(x=10, y=5)
            self.co_chcesz.place(x=10, y=40)

            # przyciski 1
            self.dodaj_form.place(x=10, y=90)

            # przycisk2
            self.usun_form.place(x=10, y=140)

            # przycisk3
            self.show_lok.place(x=10, y=190)


        elif self.login == 'admin' and self.haslo == 'admin1':

            self.Frame_zalogowany_admin.tkraise()
            self.Frame_current = 'zalogowano'
            self.czyszczenie_okna()
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

            self.label6.place(x=10,y=10)
            self.kreska6.place(x=0,y=75)
            self.tekst6.place(x=0,y=100)
            self.pusty_tekst6.place(x=150,y=391)
            self.admin.place(relx=0.5, rely=0.5, anchor='center')


        else:
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.entry1.focus_set()
            self.pokazywanie_komunikatow('zle haslo lub login sprobuj jeszcze raz','red')

    # metoda : okno kiedy wybierzemy ze chcemy dodac formatke
    def dodaj_formatke_gui(self):
        self.kod = self.entry3.get()
        self.lokalizacja = self.entry4.get().lower()
        try:
            self.ilosc = int(self.entry5.get())
        except:
            self.pokazywanie_komunikatow('Blad ilosc formatki musi byc liczba sprobuj jeszcze raz!!!', 'red')
            self.entry3.delete(0, 'end')
            self.entry4.delete(0, 'end')
            self.entry5.delete(0, 'end')
            self.entry3.focus_set()
            return
        if len(self.kod) != 4:
            self.pokazywanie_komunikatow('Blad kod formatki powinnien miec 4 liczby , sproboj jeszcze raz', 'red')
            self.entry3.delete(0, 'end')
            self.entry4.delete(0, 'end')
            self.entry5.delete(0, 'end')
            self.entry3.focus_set()
            return
        self.magazyn = klassy.MagazynP()
        self.magazyn.z_plik()
        self.formatka = klassy.Formatka(self.lokalizacja, self.kod, self.ilosc)
        self.wynik = self.magazyn.dodaj_formatke(self.formatka.to_dict())
        self.pusty_tekst.config(text=self.wynik)
        self.magazyn.to_plik()
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry3.focus_set()
        if self.wynik == '\nDodano pomyslnie':
            self.pokazywanie_komunikatow(self.wynik, 'blue')
        else:
            self.pokazywanie_komunikatow(self.wynik, 'red')

    #metoda do usuwania formatki
    def usun_formatke_GUI(self):
        self.kod1 = self.entry33.get()
        self.lokalizacja1 = self.entry44.get().lower()
        try:
            self.ilosc1 = int(self.entry55.get())
        except:
            self.pokazywanie_komunikatow('Blad ilosc formatki musi byc liczba sprobuj jeszcze raz!!!', 'red')
            self.entry33.delete(0, 'end')
            self.entry44.delete(0,'end')
            self.entry55.delete(0, 'end')
            self.entry33.focus_set()
            return

        if len(self.kod1) != 4:
            self.pokazywanie_komunikatow('Blad kod formatki powinnien miec 4 liczby , sproboj jeszcze raz', 'red')
            self.entry33.delete(0, 'end')
            self.entry44.delete(0, 'end')
            self.entry55.delete(0, 'end')
            self.entry33.focus_set()
            return


        self.magazyn1 = klassy.MagazynP()
        self.magazyn1.z_plik()

        self.formatka1 = klassy.Formatka(self.lokalizacja1, self.kod1, self.ilosc1)
        self.wynik1=self.magazyn1.pobierz_formatke(self.formatka1.to_dict())
        self.pusty_tekst1.config(text=self.wynik1)
        self.magazyn1.to_plik()

        self.entry33.delete(0, 'end')
        self.entry44.delete(0, 'end')
        self.entry55.delete(0, 'end')
        self.entry33.focus_set()





        if self.wynik1 == '\nUsunieto pomyslnie':
            self.pokazywanie_komunikatow(self.wynik1, 'blue')
        else:
            self.pokazywanie_komunikatow(self.wynik1, 'red')


    #metoda do pokazywania lokalizacji
    def pokaz_lokalizacje(self):
        self.kod11=self.entry333.get()
        self.magazyn11=klassy.MagazynP()
        self.magazyn11.z_plik()
        self.wynik11=self.magazyn11.pokaz_lokl(self.kod11)

        if self.wynik11 is None:
            self.pokazywanie_komunikatow(f'Kodu ({self.kod11}) nie ma na magazynie !!', 'red')
        else:
            tekst= '\n'.join(self.wynik11)
            self.pokazywanie_komunikatow(tekst, 'blue')







    #metoda do pokazywania tekstu
    def pokazywanie_komunikatow(self, wynik, kolor):
        if self.Frame_current == 'dodaj':
            aktualny_tekst=self.pusty_tekst.cget('text')
            if aktualny_tekst == wynik:
                self.pusty_tekst.config(text='',fg='black')
                self.pusty_tekst.after(100,lambda:self.pusty_tekst.config(text=wynik,fg=kolor))
            else:
                self.pusty_tekst.config(text=wynik,fg=kolor)
        if self.Frame_current == 'usun':
            aktualny_tekst=self.pusty_tekst1.cget('text')
            if aktualny_tekst == wynik:
                self.pusty_tekst1.config(text='',fg='black')
                self.pusty_tekst1.after(100,lambda:self.pusty_tekst1.config(text=wynik,fg=kolor))
            else:
                self.pusty_tekst1.config(text=wynik,fg=kolor)
        if self.Frame_current == 'pokaz':
            aktualny_tekst = self.pusty_tekst11.cget('text')
            if aktualny_tekst == wynik:
                self.pusty_tekst11.config(text='',fg='black',font=('Courier',20))
                self.pusty_tekst11.after(100,lambda:self.pusty_tekst11.config(text=wynik,fg=kolor))
            else:
                self.pusty_tekst11.config(text=wynik,fg=kolor,font=('Courier',20))
        if self.Frame_current == 'logowanie':
            aktualny_tekst = self.zle_haslo.cget('text')
            if aktualny_tekst == wynik:
                self.zle_haslo.config(text='',fg='red')
                self.zle_haslo.after(100,lambda:self.zle_haslo.config(text=wynik,fg=kolor))
            else:
                self.zle_haslo.config(text=wynik,fg='red')



    # metoda do cofania linije za pomoca backspace
    def backspace(self, event):
        self.wybrane_pole = event.widget
        #logwanie
        if self.wybrane_pole == self.entry2 and self.entry2.get() == '':
            self.entry1.focus_set()

        #dodaj formatke
        if self.wybrane_pole == self.entry4 and self.entry4.get() == '':
            self.entry3.focus_set()
        if self.wybrane_pole == self.entry5 and self.entry5.get() == '':
            self.entry4.focus_set()

        #usun formatke
        if self.wybrane_pole == self.entry44 and self.entry44.get() == '':
            self.entry33.focus_set()
        if self.wybrane_pole == self.entry55 and self.entry55.get() == '':
            self.entry44.focus_set()



    #metoda do wszystkich bindow
    def bindy(self):
        #bindy enter
        #logowanie
        self.entry1.bind('<Return>', lambda event: self.entry2.focus_set())
        self.entry2.bind('<Return>', self.zalogowano)


        #dodaj
        self.entry3.bind('<Return>', lambda event: self.entry4.focus_set())
        self.entry4.bind('<Return>', lambda event: self.entry5.focus_set())
        self.entry5.bind('<Return>', lambda event: self.dodaj_formatke_gui())

        #usun
        self.entry33.bind('<Return>', lambda event: self.entry44.focus_set())
        self.entry44.bind('<Return>',lambda event : self.entry55.focus_set())
        self.entry55.bind('<Return>', lambda event: self.usun_formatke_GUI())

        #pokaz
        self.entry333.bind('<Return>', lambda event: self.pokaz_lokalizacje())



        #bindy backspace
        self.entry2.bind('<BackSpace>', self.backspace)
        self.entry4.bind('<BackSpace>', self.backspace)
        self.entry5.bind('<BackSpace>', self.backspace)
        self.entry44.bind('<BackSpace>', self.backspace)
        self.entry55.bind('<BackSpace>', self.backspace)

        #cofanie strony f3
        self.bind('<F3>', self.cofnij_strone)


        #bind to metody pomocnicznej
        self.bind("<Button-1>", self.pokaz_kordy)
        self.pokazac = False  #<-- jesli chcemy metode pomocnicza zmieniam na True

    #metoda do cofania stron
    def cofnij_strone(self, event):
        if self.Frame_current == 'dodaj' or self.Frame_current == 'usun' or self.Frame_current == 'pokaz':
            if self.Frame_current == 'dodaj':
                self.entry3.delete(0, 'end')
                self.entry4.delete(0, 'end')
                self.entry5.delete(0, 'end')
                self.entry3.focus_set()
                self.pusty_tekst.config(text='')
            if self.Frame_current == 'usun':
                self.entry33.delete(0, 'end')
                self.entry44.delete(0, 'end')
                self.entry55.delete(0, 'end')
                self.entry33.focus_set()
                self.pusty_tekst1.config(text='')
            if self.Frame_current == 'pokaz':
                self.entry333.delete(0, 'end')
                self.pusty_tekst11.config(text='')





            self.Frame_zalogowany.tkraise()
            self.Frame_current = 'zalogowano'
            self.welcom.place(x=10, y=5)
            self.co_chcesz.place(x=10, y=40)
            self.dodaj_form.place(x=10, y=90)
            self.usun_form.place(x=10, y=140)
            self.show_lok.place(x=10, y=190)


        elif self.Frame_current == 'zalogowano':
            self.pusty_tekst6.config(text='')
            self.Frame_logowanie.tkraise()
            self.entry1.focus_set()
            self.Frame_current = 'logowanie'
            self.label1.place(x=238, y=165)
            self.entry1.place(x=306, y=167)
            self.kreska1.place(x=306, y=190)
            self.label2.place(x=238, y=202)
            self.entry2.place(x=347, y=204)
            self.kreska2.place(x=347, y=227)
            self.zle_haslo.config(text='')
            self.zle_haslo.place(x=230,y=235)


    # metoda pomocnicza do pokazywania wsplozendnych x i y
    def pokaz_kordy(self, event):
        if self.pokazac:
            print(f'x={event.x} ,y={event.y}')
