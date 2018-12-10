class Node:
    def __init__(self, val):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, val):
        node = Node(val)
        self.head = node
    
    def addNode(self, val):
        node = Node(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self):
        runner = self.head    
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
      
my_list = SList(10)
my_ist.addNode(9)
my_list.addNode(5)
my_list.addNode(11)
my_list.removeNode(9)
my_list.removeNode(10)

my_list.printAllValues("Attempt 1")


