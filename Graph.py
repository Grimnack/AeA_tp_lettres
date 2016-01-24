# TP lettre qui saute 
# Arnaud Cojez et Matthieu Caron
import Dicos
from collections import deque

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
        self.listeMot = listeMot
        self.dejaVu = [False]*len(self.listeMot)
        self.pere = [-1] * len(self.listeMot)
        self.chemin = []

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
        self.dejaVu[x] = True
        # print(self.listeMot[x])
        self.chemin.append(self.listeMot[x])
        for fils in self.succ[x] :
            if not self.dejaVu[fils] :
                self.DFS(fils)

    def visit(self) :
        self.dejaVu = [False]*len(self.listeMot)
        for x in range(len(self.dejaVu)) :
            if(not self.dejaVu[x]) :
                self.chemin = []
                self.DFS(x)
                print(self.chemin)



    def getIndice(self, mot) :
        for i in range(len(self.listeMot)) :
            if mot == self.listeMot[i] :
                return i
        print(mot, "pas trouvé")
        return -1
                
    def DFS_profondeur(self,x) :
        self.dejaVu[x] = True
        # print(self.listeMot[x])
        self.chemin.append(self.listeMot[x])
        for fils in self.succ[x] :
            if not self.dejaVu[fils] :
                self.pere[fils] = x
                self.DFS_profondeur(fils)

    def visit_profondeur(self) :
        self.dejaVu = [False]*len(self.listeMot)
        for x in range(len(self.dejaVu)) :
            if(not self.dejaVu[x]) :
                self.chemin = []
                self.DFS_profondeur(x)
                print(self.chemin)

    def chemin_profondeur(self, mot1, mot2):
        parcours = []
        self.DFS_profondeur(self.getIndice(mot1))
        actuel = self.getIndice(mot2)
        while self.pere[actuel] != -1 :
            parcours.append(self.listeMot[actuel])
            actuel = self.pere[actuel]
        parcours.append(self.listeMot[actuel])
        print(parcours)

    def BFSIteratif(self, racine) :
        toVisit = deque([racine])
        parcours = []
        self.dejaVu = [False]*len(self.listeMot)
        pere = [-1] * len(self.listeMot)

        #tant qu'il y a qqch dans la file
        while toVisit :
            #on depop 
            x = toVisit.popleft()
            #si on a pas deja parcouru le mot
            if not self.dejaVu[x] :
                #on l'ajoute a la liste des parcourus
                parcours.append(self.listeMot[x])
                #on ajoute ses succ a la file des sommets a parcourir
                for successeur in self.succ[x] :
                    if not self.dejaVu[successeur] :
                        pere[successeur] = x #j'ajoute le père pour créer l'arbre
                        toVisit.append(successeur)
                self.dejaVu[x] = True
                
        # print(parcours)
        return pere

    def afficheChemin(self, feuille, pere):
        parcours = []
        actuel = feuille
        while pere[actuel] != -1 :
            parcours.append(self.listeMot[actuel])
            actuel = pere[actuel]
        parcours.append(self.listeMot[actuel])
        print(parcours)
    

                
                
petiteliste = ["gag", "gay", "guy", "bob"]
listeMot =  ["gag", "gai", "gaz", "gel", "gks", 
             "gin", "gnu", "glu", "gui", "guy", "gre", "gue", 
             "ace", "acm", "agi", "ait", "aie", "ail", 
             "air", "and", "alu", "ami", "arc", "are", 
             "art", "apr", "avr", "sur", "mat", "mur" ]

# print(listeMot)
# graph = Graph(petiteliste)
graph = Graph(Dicos.dico4)
graph.lettreQuiSaute()
# graph.visit_profondeur()
# print(graph.succ)

graph.chemin_profondeur("lion","peur")


# graph.DFS(0)
#graph.DFS(1)
#graph.DFS(2)
#graph.DFS(3)

# pere = graph.BFSIteratif(graph.getIndice("lion"))
# print(pere)
# graph.afficheChemin(graph.getIndice("peur"),pere)

# graph3 = Graph(Dicos.dico3)
# graph3.lettreQuiSaute()
# graph3.visit()
