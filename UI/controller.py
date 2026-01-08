import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def aggiorna_lista_auto(self, e): #se metto "e" la funzione si attiva solo se avviene l'evento e
        self._view.lista_auto.controls.clear()  # ripulisco la ListView
        lista_auto = self._model.get_automobili()  # lista di oggetti automobile
        if lista_auto is not None: #se la lista non è vuota
            if len(lista_auto) > 0: #se la lista contiene elementi
                for auto in lista_auto:
                    stato = "✅" if auto.disponibile else "⛔"
                    self._view.lista_auto.controls.append(ft.Text(f"{stato} {auto}"))
                    #la ListView accetta solo stringhe, non posso passarle direttamente l'oggetto auto
                    #ft.Text() prende l'auto in formato stringa
                self._view.update()
            else:
                self._view.show_alert("Non ci sono automobili")
        else:
            self._view.show_alert("Non connesso al database")

    def cerca_automobili_per_modello(self, e):
        self._view.lista_auto_ricerca.controls.clear()
        modello = self._view.input_modello_auto.value #viene dall'interfaccia utente
        lista_auto_trovate= self._model.cerca_automobili_per_modello(modello) #funzione implementata nel model

        if lista_auto_trovate is not None:
            if len(lista_auto_trovate) > 0:
                for auto in lista_auto_trovate:
                    self._view.lista_auto_ricerca.controls.append(ft.Text(f"{auto}"))
                self._view.update()
            else:
                self._view.show_alert("Nessun automobile trovata")
        else:
            self._view.show_alert("Non connesso al database")

