from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo, numPrese):
        super().__init__(codiceUnivoco, supMetriQuad, padiglione, prezzo)
        self._numPrese = int(numPrese)

    @property
    def prezzo_finale(self):
        return self._prezzo * (1 + 0.07 * self._numPrese)