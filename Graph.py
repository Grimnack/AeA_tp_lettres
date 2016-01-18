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
        self.listeMot = listeMot
        self.dejaVu = [False]*len(self.listeMot)
        self.pere = [-1]*len(self.listeMot)
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
                
    def DFS_chemin(self,x) :
        self.dejaVu[x] = True
        # print(self.listeMot[x])
        self.chemin.append(self.listeMot[x])
        for fils in self.succ[x] :
            if not self.dejaVu[fils] :
                if self.pere[fils] != -1 :
                    self.pere[fils] = x
                self.DFS_chemin(fils)

    def visit_chemin(self) :
        self.dejaVu = [False]*len(self.listeMot)
        self.pere = [-1]*len(self.listeMot)
        for x in range(len(self.dejaVu)) :
            if(not self.dejaVu[x]) :
                self.chemin = []
                self.DFS_chemin(x)
                #print(self.chemin)

    #marche pas
    def print_chemin(self, mot1, mot2) :
        self.visit_chemin()
        chemin = []
        imot1 = self.getIndice(mot1)
        imot2 = self.getIndice(mot2)
        i = imot2
        while i != imot1:
            chemin.append(self.listeMot[i])
            i = self.pere[i]
            print(chemin)
        print(i, imot1)
        if i != -1 and i == imot1 :
            chemin.append(self.listeMot[i])
            print(chemin.reverse())
        else :
            print("a pas chemin huhuhh")
        
                
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
# print(graph.succ)



# graph.DFS(0)
#graph.DFS(1)
#graph.DFS(2)
#graph.DFS(3)

graph.print_chemin("lion", "peur")

# graph3 = Graph(Dicos.dico3)
# graph3.lettreQuiSaute()
# graph3.visit()
