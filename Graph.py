# TP lettre qui saute 
# Arnaud Cojez et Matthieu Caron
import Dicos

def diffUneLettre(mot1, mot2):
    if len(mot1) != len(mot2) :
        return False
    cpt = 1
    for i in range(len(mot1)) :
        if mot1[i] != mot2[i] :
            cpt -= 1
    return cpt == 0


class Graph(object):
    """docstring for Graph"""
    def __init__(self, listeMot):
        super(Graph, self).__init__()
        tab = []
        for mot in listeMot :
            tab.append([])
        self.succ = tab #tableau de list de longueur listeMot
        self.pere = [-1]*len(self.listeMot)
        self.listeMot = listeMot
        self.dejaVu = [False]*len(self.listeMot)

    def AjouterArete (self, s, d) :
        """ajoute s à la liste des successeurs de d et d à celle de s, 
        les mots d'indices s et d étant supposés différer d'une lettre"""
        self.succ[s].append(d)
        self.succ[d].append(s)

    

    def lettreQuiSaute(self) :
        """initialise les listes de successeurs selon la règle du jeu de la lettre qui saute."""
        for i in range(len(self.listeMot)) :
            for j in range(i+1,len(self.listeMot)) :
                if diffUneLettre(self.listeMot[i],self.listeMot[j]) :
                    self.AjouterArete(i,j)

    def DFS(self,x) :
        parcours = [self.listeMot[x]]
        self.dejaVu[x] = True
        indice = x
        trouve = True
        while trouve:
            trouve = False
            for imot in self.succ[indice] :
                if(not self.dejaVu[imot]) :
                    indice = imot
                    self.dejaVu[imot] = True
                    parcours.append(self.listeMot[indice])
                    trouve = True
                    break
        print(parcours)

    def visit(self) :
        self.dejaVu = [False]*len(self.listeMot)
        for x in range(len(self.dejaVu)) :
            if(not self.dejaVu[x]) :
                self.DFS(x)

    #TODO ######################################################################""
    def DFS(self,x) :
        parcours = [self.listeMot[x]]
        self.dejaVu[x] = True
        indice = x
        trouve = True
        while trouve:
            trouve = False
            for imot in self.succ[indice] :
                if(not self.dejaVu[imot]) :
                    indice = imot
                    self.dejaVu[imot] = True
                    parcours.append(self.listeMot[indice])
                    trouve = True
                    break
        print(parcours)

    def visit(self) :
        self.dejaVu = [False]*len(self.listeMot)
        for x in range(len(self.dejaVu)) :
            if(not self.dejaVu[x]) :
                self.DFS(x)


petiteliste = ["gag", "gay", "guy", "bob"]
listeMot =  ["gag", "gai", "gaz", "gel", "gks", 
             "gin", "gnu", "glu", "gui", "guy", "gre", "gue", 
             "ace", "acm", "agi", "ait", "aie", "ail", 
             "air", "and", "alu", "ami", "arc", "are", 
             "art", "apr", "avr", "sur", "mat", "mur" ]

# print(listeMot)
# graph = Graph(petiteliste)
graph = Graph(listeMot)
graph.lettreQuiSaute()
# print(graph.succ)

#graph.DFS(0)
#graph.DFS(1)
#graph.DFS(2)
#graph.DFS(3)

graph.visit()

# graph3 = Graph(Dicos.dico3)
# graph3.lettreQuiSaute()
# graph3.visit()
