from database.DB_connect import get_connection
from model.automobile import Automobile


def get_automobili(self) -> list[Automobile] | None:
    """
        Funzione che legge tutte le automobili nel database
        :return: una lista con tutte le automobili presenti oppure None
    """

    connessione = get_connection()
    risultati = []
    if connessione is not None:  # vedo se si è collegato
        cursore = connessione.cursor(dictionary=True)
        # dictionary=True, creo gli oggetti che ricevo dal database come dei dizionari
        query = 'SELECT * FROM automobile'
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

    connessione = get_connection()
    risultati = []
    if connessione is not None:  # vedo se si è collegato
        cursore = connessione.cursor(dictionary=True)
        # dictionary=True, creo gli oggetti che ricevo dal database come dei dizionari
        query = 'SELECT * FROM automobile WHERE automobile.modello = %s'  # %s è il parametro
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