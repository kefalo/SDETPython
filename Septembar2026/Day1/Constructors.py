# Example of classes and methods without constructor
# no need for construct. as methods of it's class doesn't need construct(class doesn't save anything) it has it's own parameters and can work that way
class Matematika:
    # Nema konstruktora!

    # Metoda koja VRAĆA vrednost
    def saberi(self, a, b):
        return a + b

    # Metoda koja samo ODRADI POSAO (ne vraća ništa)
    def ispisi_poruku(self, tekst):
        print(f"[LOG]: {tekst}")

# Pravimo objekat bez parametara
mat = Matematika()

# Obe metode rade normalno
rezultat = mat.saberi(10, 5)        # Vraća 15
mat.ispisi_poruku("Sve radi!")     # Samo ispisuje na ekranu

# Now example of the class with methods where class needs to save values in order to work(perform operations as per design), which needs constructor
class Korisnik:
    def __init__(self, ime):
        self.ime = ime  # Objekat je zapamtio ime

    # Metoda koja VRAĆA vrednost (koristi zapamćeno ime)
    def vrati_veliko_ime(self):
        return self.ime.upper()

    # Metoda koja samo ODRADI POSAO (koristi zapamćeno ime)
    def pozdravi(self):
        print(f"Zdravo, ja sam {self.ime}!")

# Pravimo objekat i ODMAH mu dajemo podatak kroz konstruktor
korisnik1 = Korisnik("Marko")

# Obe metode imaju pristup podatku iz konstruktora
ime_veliko = korisnik1.vrati_veliko_ime()  # Vraća "MARKO"
korisnik1.pozdravi()                       # Samo ispisuje: Zdravo, ja sam Marko!


# Example of the class with constructor when class and methods must use permanent memory to save something
class KorpaZaKupovinu:
    def __init__(self, ime_kupca):
        self.kupac = ime_kupca  # Trajno pamti ko je vlasnik korpe
        self.proizvodi = []     # Trajna memorija (prazna lista na početku)

    # Metoda koja samo ODRADI POSAO (dodaje u memoriju, ne vraća ništa)
    def dodaj_proizvod(self, naziv_proizvoda):
        self.proizvodi.append(naziv_proizvoda)
        print(f"Dodato: {naziv_proizvoda} u korpu korisnika {self.kupac}")

    # Metoda koja VRAĆA vrednost (čita iz memorije)
    def izbroj_proizvode(self):
        return len(self.proizvodi)

# --- UPOTREBA U APLIKACIJI ---
# Marko i Ana kupuju u isto vreme. Pravimo dva posebna objekta.
korpa_marko = KorpaZaKupovinu("Marko")
korpa_ana = KorpaZaKupovinu("Ana")

# Markova korpa trajno pamti njegove proizvode
korpa_marko.dodaj_proizvod("Laptop")
korpa_marko.dodaj_proizvod("Miš")

# Proveravamo stanje (metoda vraća vrednost iz memorije)
print(korpa_marko.izbroj_proizvode())  # Ispisuje: 2
print(korpa_ana.izbroj_proizvode())    # Ispisuje: 0 (Anina korpa je prazna i nezavisna)



# Example when class and methods doesn't need to store any parameter(value) during it's operation(usage)
class KalkulatorPopusta:
    # NEMA KONSTRUKTORA! Python sve rešava sam.
    # Klasa nema nikakvu svoju memoriju.

    # Metoda koja VRAĆA vrednost (računa na licu mesta)
    def izracunaj_snizenje(self, puna_cena, procenat_popusta):
        usteda = puna_cena * (procenat_popusta / 100)
        return puna_cena - usteda

    # Metoda koja samo ODRADI POSAO (ispisuje obaveštenje)
    def prikazi_akciju(self, naziv_akcije):
        print(f"!!! AKCIJA: {naziv_akcije} !!!")

# --- UPOTREBA U APLIKACIJI ---
# Pravimo samo jedan objekat alata koji može da koristi cela aplikacija
alkat_za_popust = KalkulatorPopusta()

# Koristimo ga za Marka
cena_za_marka = alkat_za_popust.izracunaj_snizenje(1000, 10) # Proizvod od 1000e na 10% popusta
print(f"Marko plaća: {cena_za_marka} EUR")  # Ispisuje: 900.0

# Koristimo ISTI objekat za Anu, jer objekat ništa ne pamti od malopre
cena_za_anu = alkat_za_popust.izracunaj_snizenje(50, 20)
print(f"Ana plaća: {cena_za_anu} EUR")      # Ispisuje: 40.0


"""Korpa (__init__ postoji): Svaki objekat ljubomorno čuva svoje podatke (self.proizvodi). 
Ako obrišemo objekat korpa_marko, gubimo i podatke o njegovim proizvodima.

Kalkulator (bez __init__): Objekat služi samo kao "mašina" kroz koju prođu podaci. 
Možemo ga upotrebiti milion puta za milion različitih kupaca, jer on u sebi ne zadržava ništa."""