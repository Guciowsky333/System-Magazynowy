import json



#kalsa formatki ktora ma lokalizacje kod i ilosc pojemnikow
class Formatka:
    def __init__(self,lokalizacja,kod,ilosc):
        self.kod = kod
        self.lokalizacja = lokalizacja
        self.ilosc = ilosc

    #zwracamy formatke jako slownik
    def to_dict(self):
        return {self.lokalizacja:{self.kod:{'ilosc':self.ilosc}}}




#klasa magazynP
class MagazynP:
    #caly magazyn ktory ma liste ze wszytkimi formatkami
    # i ich lokalizacjami i ilosciami
    def __init__(self):
        self.caly_magazyn={}
        lokal=[]

        #Wszytskie lokalizacje na magazynie
        #regal O
        for xx in range(1,10):
            for yy in range(1,5):
                key=f'o10{str(xx)}0{str(yy)}'
                lokal.append(key)

        for x in range(10,31):
            for y in range(1,5):
                key=f'o1{str(x)}0{str(y)}'
                lokal.append(key)
        #regal P
        for aa in range(1,10):
            for bb in range(1,5):
                key=f'p10{str(aa)}0{str(bb)}'
                lokal.append(key)

        for a in range(10, 31):
            for b in range(1, 5):
                key = f'p1{str(a)}0{str(b)}'
                lokal.append(key)
        #dodajemy wystzkie lokalizacje do slownika
        for lokalizacja in lokal:
            self.caly_magazyn[lokalizacja] = {}





    def dodaj_formatke(self,formatka):
        lokalizacja = list(formatka.keys())[0]              #lokalizacja np O10103
        kod = list(formatka[lokalizacja].keys())[0]         #kod np 7743
        ile = formatka[lokalizacja][kod]['ilosc']           #ilosc pojemnikow 7743 na lokalizacji O10103
        max=28    #maksymalna ilosc pojemnikow na jednej lokalizacji
        max_kodow=2      #maksymalna liczba kodow na lokalizacji

        if kod == '' or len(kod) >4:
            return 'Bledny kod sprobuj jeszcze raz'
        # jesli uzytkownik pod zla lokalizacje
        if lokalizacja not in self.caly_magazyn:
            return f'Lokalizacji {lokalizacja} nie ma na magazynie !!!!'


        # liczba poj na tej lokalizacji
        liczba_poj = sum(self.caly_magazyn[lokalizacja][k]['ilosc'] for k in self.caly_magazyn[lokalizacja])
        ile_poj = liczba_poj + ile  # liczba wszytskich pojemnikow razem z tymi ktorem chcemy dodac

        obecna_liczba_k=len(self.caly_magazyn[lokalizacja])   #obecna ilosc kodow na lokalizacji


        #tutaj sprawdzamy czy na palecie sa juz 2 kody
        if kod not in self.caly_magazyn[lokalizacja] and obecna_liczba_k +1 > max_kodow:
            return f' BLAD !!! na lokalizacji {lokalizacja} sa juz dwa kody a maksymalnie moga byc dwa na palecie'

        # jesli chcemy dodac wiecej niz 28 pojemnikow na jedna lokalizacji
        if ile_poj > max:
            return f'BALD !!! zbyt duza ilosc pojemnikow na jedna lokalizacje mozesz dodac maksymalnie 28 pojemnikow'


        #jesli kod jest juz w lokalizacji to dodajmy tylko ilosc
        if kod in self.caly_magazyn[lokalizacja]:
            # jesli chcemy dodac wiecej niz 28 pojemnikow na jedna lokalizacji


            self.caly_magazyn[lokalizacja][kod]['ilosc'] += ile
            return '\nDodano pomyslnie'


        #Dodajmy kod na lokalizacje
        self.caly_magazyn[lokalizacja][kod] = {'ilosc':ile}
        return '\nDodano pomyslnie'



    def pobierz_formatke(self,formatka):
        lokalizacja = list(formatka.keys())[0]           #lokalizacja np O10103
        kod = list(formatka[lokalizacja].keys())[0]      #kod np 7743
        ile = formatka[lokalizacja][kod]['ilosc']        #ilosc pojemnikow 7743 na lokalizacji O10103



        #jesli lokalizacji nie ma na magazynie
        if lokalizacja not in self.caly_magazyn:
            return f'Lokalizacji {lokalizacja} nie ma na magazynie !!!!'



        #jesli formatki nie ma na tej lokalizacji
        if kod not in self.caly_magazyn[lokalizacja]:
            return f'Formatki {kod} nie ma na lokalizacji {lokalizacja}'

        aktualny_stan = self.caly_magazyn[lokalizacja][kod]['ilosc']

        # jesli nie ma tyle na tej lokalizacji
        if aktualny_stan < ile:
            return f'BLAD !! Na lokalizacji {lokalizacja} jest tylko {aktualny_stan} formatek a ty probujesz pobrac {ile}'

        #usuwamy ilosc z lokalizcji
        self.caly_magazyn[lokalizacja][kod]['ilosc'] -= ile




        #jesli stan = 0  usuwamy ta formatke z lokalizacji
        if self.caly_magazyn[lokalizacja][kod]['ilosc'] == 0:
            del self.caly_magazyn[lokalizacja][kod]
        return '\nUsunieto pomyslnie'

    def pokaz_lokl(self,kod):
        wynik={}


        for lokalizacja,kody in self.caly_magazyn.items():
            if kod in kody:
                wynik[lokalizacja]=kody[kod]['ilosc']
        if not wynik:
            return
        wynik_posortowanych = sorted(wynik.items(),key=lambda x:x[1],reverse=True)
        return[f'{i+1}.{lokalizacja:<15} - {ilosc:>15} szt'for i,(lokalizacja,ilosc) in enumerate(wynik_posortowanych)]





    def wyczysc_magazyn(self):
        for lokalizacje in self.caly_magazyn:
            self.caly_magazyn[lokalizacje]={}







    #dajemy cala liste do pliku
    def to_plik(self):
        with open('Magazyn.json','w',encoding='utf-8')as plik:
            json.dump(self.caly_magazyn,plik,indent=4,ensure_ascii=False)



    #tutaj wczytujemy plik
    def z_plik(self):
        try:
            with open('Magazyn.json','r',encoding='utf-8')as plik:
                self.caly_magazyn=json.load(plik)
        except(FileNotFoundError,json.decoder.JSONDecodeError):
            self.caly_magazyn={}
        return self.caly_magazyn
