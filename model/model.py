from unittest import result

from mysql.connector.errorcode import WARN_NON_ASCII_SEPARATOR_NOT_IMPLEMENTED

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

        try:
            connessione = get_connection()
            cursore=connessione.cursor(dictionary=True)
            query='SELECT * FROM automobili'
            cursore.execute(query)
            risultato=cursore.fetchall()  #legge tutte le righe rimanenti e restituisce un elenco

            if not risultato:
                return None

            for riga in risultato:
                automobili=Automobile(
                        targa= riga['targa'],
                        marca=riga['marca'],
                        modello=riga['modello'],
                        anno=riga['anno'],
                        posti=riga["posti"],
                        disponibile=riga["disponibile"]
                )
            cursore.close()
            connessione.close()
            return automobili

        except Exception as e:
            print(e)
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            connessione = get_connection()
            cursore = connessione.cursor(dictionary=True)

            query = "SELECT * FROM automobile WHERE modello LIKE %s"
            cursore.execute(query, (f"%{modello}%",))
            result = cursore.fetchall()

            if not result:
                return None

            for riga in result:
                automobili = Automobile(
                        targa=riga["targa"],
                        marca=riga["marca"],
                        modello=riga["modello"],
                        anno=riga["anno"],
                        posti=riga["posti"],
                        disponibile=riga["disponibile"]
                    )

            cursore.close()
            connessione.close()
            return automobili

        except Exception as e:
            print(e)
            return None