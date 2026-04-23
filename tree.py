from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

Demanda = Node("Demanda")

Residencial = Node("Residencial", parent= Demanda, bgcolor="#36495A", color="white")
Urbano = Node("Urbano", parent= Residencial, bgcolor="#36495A", color="white")
Rural = Node("Rural", parent= Residencial, bgcolor="#36495A", color="white")

Industrial = Node("Industrial", parent= Demanda, bgcolor='#FBAA1B', color="white")
EAIMCS = Node("EAIMCS", parent= Industrial, bgcolor='#FBAA1B', color="white")
MIPES = Node("MIPES", parent= Industrial, bgcolor='#FBAA1B', color="white")

Transporte = Node("Transporte", parent= Demanda, bgcolor='#207653', color="white")
Carretero = Node("Carretero", parent= Transporte, bgcolor='#207653', color="white")
Aereo = Node("Aereo", parent= Transporte, bgcolor='#207653', color="white")
Ferroviario = Node("Ferroviario", parent= Transporte, bgcolor='#207653', color="white")
Fluvial = Node("Fluvial", parent= Transporte, bgcolor='#207653', color="white")
Teleferico = Node("Teleferico", parent= Transporte, bgcolor='#207653', color="white")

CyP = Node("CyP", parent= Demanda, bgcolor='#8FC73E', color="black")
APyM = Node('APyM', parent= Demanda, bgcolor='#A1140B', color="white")
Construcción = Node("Construcción", parent= Demanda, bgcolor='#6D6F70', color="white")


# ~ UniqueDotExporter(Demanda).to_picture("tree-demanda.svg")
UniqueDotExporter(Demanda, nodeattrfunc=lambda node: f'shape="box" label="{node.name}" fontname="louis george" style="filled" fillcolor="{getattr(node, "bgcolor", "white")}" fontcolor="{getattr(node, "color", "black")}"').to_picture("tree-demanda.svg")
