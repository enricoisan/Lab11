import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = None
        self._graph = nx.Graph()

    def getColors(self):
        return DAO.getColors()

    def buildGraph(self, color, year):

        # Inizializzo il grafo
        self._graph.clear()

        # Aggiungo i nodi
        self._nodes = DAO.getNodes(color)
        self._graph.add_nodes_from(self._nodes)

        # Aggiungiamo gli archi
        for node1 in self._nodes:
            for node2 in self._nodes:
                if node1 != node2:
                    w = DAO.getWeight(node1, node2, year)
                    if w[0] > 0:
                        self._graph.add_edge(node1, node2, weight = w[0])
        return

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getAllEdges(self):
        return self._graph.edges()

    def getAllNodes(self):
        return self._nodes()

    def getTopThreeEdge(self):
        edgesSorted = sorted(self._graph.edges(data=True), key = lambda x: x[2]['weight'], reverse = True)
        return edgesSorted[:3]













