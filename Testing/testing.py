from time import time
from __init__ import printSwitch
from graph.Graph import GraphBase
import  random

numVertici=[10, 20, 50, 100, 1000, 10000]
numArchi=[10, 50, 100, 1000, 10000,100000]
inputType = 0  # 1 crescente, -1 decrescente, 0 random

for item in numVertici:
 g = GraphBase()
 for i in range(0, item):
     if inputType == 1:
         g.addNode(i)
         g.insertEdge(i, random.randint(0, i), random.randint(0, 10))
     elif inputType == -1:
         g.addNode(item - i)
         g.insertEdge(i, random.randint(0, i), random.randint(0, 10))
     elif inputType == 0:
         g.addNode(random.randint(0, item))
         g.insertEdge(i, random.randint(0, i), random.randint(0, 10))
     else:
         raise Exception("You used an invalid inputType parameter!")
 printSwitch.dumpOperations = False



 start = time()
 g.visitaInPriorita1(random.randint(0, len(g.getNodes()) ))
 runningTime=time() - start
 print("visita con dheap required {} seconds.".format(runningTime))
 print('')

 start = time()
 g.visitaInPriorita2(random.randint(0, len(g.getNodes()) ))
 runningTime = time() - start
 print("visita con binaryheap required {} seconds.".format(runningTime))
 print('')

 if item!=10000:
  start = time()
  g.visitaInPriorita3(random.randint(0, len(g.getNodes()) ))
  runningTime=time() - start
  print("visita con binomial required {} seconds.".format(runningTime))
  print('')

for item in numArchi:
    g1 = GraphBase()
    for i in range(0, item):
        if inputType == 1:
            g1.addNode(i)
        elif inputType == -1:
            g1.addNode(item - i)
        elif inputType == 0:
            g1.addNode(random.randint(0, item))
        else:
            raise Exception("You used an invalid inputType parameter!")

    g1.insertEdge(item, random.randint(0, item), random.randint(0, 10))

    start = time()
    g1.visitaInPriorita1(random.randint(0, len(g1.getNodes())))
    runningTime = time() - start
    print("visita con dheap required {} seconds.".format(runningTime))
    print('')

    start = time()
    g1.visitaInPriorita2(random.randint(0, len(g1.getNodes())))
    runningTime = time() - start
    print("visita con binaryheap required {} seconds.".format(runningTime))
    print('')

    start = time()
    g1.visitaInPriorita3(random.randint(0, len(g1.getNodes())))
    runningTime = time() - start
    print("visita con binomial required {} seconds.".format(runningTime))
    print('')
    printSwitch.dumpOperations = False
