from model.model import Model

myModel = Model()
myGraph = myModel.buildGraph("White", "Year")
print(myGraph.nodes)