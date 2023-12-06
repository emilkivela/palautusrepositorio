from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        if len(self._syote_kentta.get()) > 0:
            arvo = int(self._syote_kentta.get())
            return arvo

    def _suorita_komento(self, komento):
        self._komennot = {
            Komento.SUMMA: Summa(self._sovelluslogiikka, self._lue_syote()),
            Komento.EROTUS: Erotus(self._sovelluslogiikka, self._lue_syote()),
            Komento.NOLLAUS: Nollaus(self._sovelluslogiikka),
        }
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class Summa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        #print(self.io)
        self.sovelluslogiikka.plus(self.io)

    
class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
    
    def suorita(self):
        self.sovelluslogiikka.plus(self.io)
    
class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        self.sovelluslogiikka.nollaa()

