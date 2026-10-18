from stand import Stand

class StandPremium(Stand):
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo, posizione):
        super().__init__(codiceUnivoco, supMetriQuad, padiglione, prezzo)
        self._posizione = posizione

    @property
    def prezzo_finale(self):
        return self._prezzo * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codiceUnivoco}"
        return f"{self._codiceUnivoco}: Premium ({self._posizione}) | {self._supMetriQuad} mq - Padiglione {self._padiglione} - Prezzo {self.prezzo_finale}€ - {stato}"