class Queue(object):
    ''' implements a FIFO queue'''

    def __init__(self):
        self.L = []

    def add(self, element):
        self.L.append(element)

    def pop(self):
        return self.L.pop(0)

    def size(self):
        return len(self.L)

    def show(self):
        print self.L


q = Queue()

q.add(1)
q.add(2)
q.add(3)

q.pop()
q.show()


class LinkedList(object):
    ''' implements linked list A -> B -> C'''

    def __init__(self):
        self.d = {}

    def append(self, element):
        last = 0
        if len(self.d) > 0:
            last = max(self.d.keys())
        self.d[last+1] = element

    def show(self):
        keylist = list(self.d.keys())
        keylist.sort()
        for k in keylist:
            print self.d[k] + " -> ",


ll = LinkedList()

ll.append("To")
ll.append("be")
ll.append("or")
ll.append("not")
ll.append("to")
ll.append("be")

ll.show()

# ------------------------------------------------------------
# Inheritance Example
class aPlayer(object):
    ''' Object for players'''
    def __init__(self, name="none", skill=0.0):
        self.name = name
        self.skill = skill

    def summary(self):
        print "%s: %.2f" %(str(self.name), float(self.skill))


class aGoalie(aPlayer):
    ''' goalie is-a Player '''
    def __init__(self, name, skill=0.0, height=0.0):
        super(aGoalie,self).__init__(name, skill)
        self.height = height


pepe = aPlayer("Pepe")
pepe.summary()

paco = aPlayer("Paco", 23)
paco.summary()

luis = aPlayer("Luis", 35.223)
luis.summary()

neuer = aGoalie("Neuer")
neuer.summary()

iker = aGoalie("Iker", 3.1, 5.9)
iker.summary()
