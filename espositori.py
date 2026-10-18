class Espositori:
    def __init__(self, codiceUnivoco, nome, cognome):
        self._codiceUnivoco = codiceUnivoco
        self._nome = nome
        self._cognome = cognome

    @property
    def codiceUnivoco(self):
        return self._codiceUnivoco

    def __eq__(self, other):
        if isinstance(other, Espositori):
            return self._codiceUnivoco == other.codiceUnivoco
        return False

    def __str__(self):
        return f"[{self._codiceUnivoco}] {self._nome} {self._cognome}"

    def __repr__(self):
        return self.__str__()