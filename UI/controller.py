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

    def mostra_automobili(self):
        #evento per il pulsante mostra
        automobili = self._model.get_automobili() #lista di oggetti automobile
        self._view.lista_auto.controls.clear() #ripulisco la ListView

        if not automobili: #se la lista è vuota
            self._view.lista_auto.controls.append(
                ft.Text("Nessuna automobile trovata nel database.")
            )
        else:
            for a in automobili:
                stato = "Disponibile ✅" if a.disponibile else "Noleggiata ❌"
                self._view.lista_auto.controls.append(
                    ft.Text(f"{a.codice} - {a.marca} {a.modello} ({a.anno}) | {a.posti} posti | {stato}")
                )

        self._view.update()

    def cerca_automobili(self):
        #evento per il pulsante cerca
        modello = self._view.input_modello_auto.value.strip()
        self._view.lista_auto_ricerca.controls.clear()

        if not modello:
            self._view.lista_auto_ricerca.controls.append(ft.Text("Inserisci un modello da cercare."))
            self._view.update()
            return

        automobili = self._model.cerca_automobili_per_modello(modello) #usa la funzione implementata nel model

        if not automobili:
            self._view.lista_auto_ricerca.controls.append(
                ft.Text(f"Nessuna automobile trovata per il modello '{modello}'.")
            )
        else: #se trovo delle automobili
            for a in automobili:
                stato = "Disponibile ✅" if a.disponibile else "Noleggiata ❌"
                self._view.lista_auto_ricerca.controls.append(
                    ft.Text(f"{a.codice} - {a.marca} {a.modello} ({a.anno}) | {a.posti} posti | {stato}")
                )

        self._view.update()
