from stand import Stand
from standPreseExtra import StandPreseExtra
from standPremium import StandPremium
from espositori import Espositori

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome=nome
        self.stands=[]
        self.espositori=[]

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome=nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            with open(file_path, "r") as filein:
                for line in filein:
                    campi=line.strip().split(",")
                    if campi[0].startswith("S"):
                        if len(campi)==4:
                            s=Stand(campi[0],campi[1],campi[2],campi[3])
                        elif campi[4].isdigit():
                            s=StandPreseExtra(campi[0],campi[1],campi[2],campi[3],campi[4])
                        else:
                            s=StandPremium(campi[0],campi[1],campi[2],campi[3],campi[4])
                        self.stands.append(s)
                    else:
                        e=Espositori(campi[0],campi[1],campi[2])
                        self.espositori.append(e)
        except FileNotFoundError:
            raise FileNotFoundError

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        espositore_trovato = None
        for e in self.espositori:
            if e.codiceUnivoco == codice_espositore:
                espositore_trovato = e

        if espositore_trovato is None:
            raise Exception(f"Errore: L'espositore {codice_espositore} non esiste.")

        stand_trovato = None
        for s in self.stands:
            if s.espositore is not None and s.espositore.codiceUnivoco == codice_espositore:
                raise Exception(
                    f"Errore: L'espositore {codice_espositore} ha già assegnato lo stand {s.codiceUnivoco}.")
            if s.codiceUnivoco == codice_stand:
                stand_trovato = s

        if stand_trovato is None:
            raise Exception(f"Errore: Lo stand {codice_stand} non esiste.")

        if not stand_trovato.disponibile:
            raise Exception(f"Errore: Lo stand {codice_stand} è già occupato.")

        stand_trovato.espositore = espositore_trovato

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        if len(self.espositori) == 0:
            print("Nessun espositore registrato nel sistema.")
            return

        for e in self.espositori:
            stand_assegnato = None
            for s in self.stands:
                if s.espositore is not None and s.espositore == e:
                    stand_assegnato = s.codiceUnivoco

            if stand_assegnato is not None:
                print(f"Espositore: {e} -> Stand assegnato: {stand_assegnato}")
            else:
                print(f"Espositore: {e} -> Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stands)