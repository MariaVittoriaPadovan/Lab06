
from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO

        connessione = get_connection()
        risultati=[]
        if connessione is not None: #vedo se si è collegato
            cursore=connessione.cursor(dictionary=True)
            #dictionary=True, creo gli oggetti che ricevo dal database come dei dizionari
            query='SELECT * FROM automobile'
            cursore.execute(query)
            for riga in cursore:
                risultati.append(Automobile(riga['codice'], riga['marca'], riga['modello'], riga['anno'], riga["posti"]))

            cursore.close()
            connessione.close()
            return risultati
        else:
            print("Connessione non trovata")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO

        connessione = get_connection()
        risultati = []
        if connessione is not None:  # vedo se si è collegato
            cursore = connessione.cursor(dictionary=True)
            # dictionary=True, creo gli oggetti che ricevo dal database come dei dizionari
            query = 'SELECT * FROM automobile WHERE automobile.modello = %s' # %s è il parametro
            cursore.execute(query, (modello,))
            for riga in cursore:
                risultati.append(
                    Automobile(riga['codice'], riga['marca'], riga['modello'], riga['anno'], riga["posti"]))

            cursore.close()
            connessione.close()
            return risultati
        else:
            print("Connessione non trovata")
            return None
