import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.years = ["2015", "2016", "2017", "2018"]
        self.colors = []


    def fillDDyear(self):
        for year in self.years:
            self._view._ddyear.options.append(ft.dropdown.Option(year))
        return

    def fillDDcolor(self):
        self.colors = self._model.getColors()
        for color in self.colors:
            self._view._ddcolor.options.append(ft.dropdown.Option(color))
        return

    def handle_graph(self, e):

        # Recupero dati di input
        self.selectedYear = self._view._ddyear.value
        self.selectedColor = self._view._ddcolor.value

        # Validazione input
        if self.selectedYear is None and self.selectedColor is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un anno e un colore"))
            self._view.update_page()
            return

        if self.selectedYear is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un anno"))
            self._view.update_page()
            return

        if self.selectedColor is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un colore"))
            self._view.update_page()
            return

        # Costruzione grafo
        self._model.buildGraph(self.selectedColor, self.selectedYear)

        # Chiama metodi del model
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Graph created!"))
        self._view.txtOut.controls.append(ft.Text("Num of nodes: " + str(self._model.getNumNodes())))
        self._view.txtOut.controls.append(ft.Text("Num of edges: " + str(self._model.getNumEdges())))
        self._view.update_page()

        # Stampa dei tre archi con peso maggiore
        for edge in self._model.getTopThreeEdge():
            self._view.txtOut.controls.append(ft.Text(f"{edge[0].Product_number} -> {edge[1].Product_number} - Peso: {edge[2]['weight']}"))
            self._view.update_page()

        # Stampa dei nodi ripetuti
        self._view.txtOut.controls.append(ft.Text("Prodotti ripetuti:"))
        repeatedNodes = self.repeatedNodes(self._model.getTopThreeEdge())
        for node in repeatedNodes:
            self._view.txtOut.controls.append(
                ft.Text(node.Product_number))
            self._view.update_page()
        return


    def repeatedNodes(self, listOfEdges):
        repeatedNodesDict = {}
        for edge in listOfEdges:
            nodo1 = edge[0]
            if nodo1 not in repeatedNodesDict.keys():
                repeatedNodesDict[nodo1] = 1
            else:
                repeatedNodesDict[nodo1] += 1
            nodo2 = edge[1]
            if nodo2 not in repeatedNodesDict.keys():
                repeatedNodesDict[nodo2] = 1
            else:
                repeatedNodesDict[nodo2] += 1
        edgesList = []
        for key in repeatedNodesDict.keys():
            if repeatedNodesDict[key] > 1:
                edgesList.append(key)
        return edgesList

    def handle_search(self, e):
        pass















