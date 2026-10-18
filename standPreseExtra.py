from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo, numPrese):
        super().__init__(codiceUnivoco, supMetriQuad, padiglione, prezzo)
        self._numPrese = int(numPrese)

    @property
    def prezzo_finale(self):
        return self._prezzo * (1 + 0.07 * self._numPrese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codiceUnivoco}"
        return f"{self._codiceUnivoco}: Prese Extra | {self._supMetriQuad} mq - Padiglione {self._padiglione} - Prezzo {self.prezzo_finale}€ - Prese aggiuntive: {self._numPrese} - {stato}"