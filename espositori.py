class Espositori:
    def __init__(self,codiceUnivoco,nome,cognome):
        self.__codiceUnivoco = codiceUnivoco
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codiceUnivoco(self):
        return self.__codiceUnivoco