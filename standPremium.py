from stand import Stand

class StandPremium(Stand):
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo, posizione):
        super().__init__(codiceUnivoco, supMetriQuad, padiglione, prezzo)
        self._posizione = posizione

    @property
    def prezzo_finale(self):
        return self._prezzo * 1.30