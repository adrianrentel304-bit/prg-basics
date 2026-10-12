treeCIR=input("Enter tree area: ")
pi = 3.14
tree = float(treeCIR)
treeDIA = tree/ pi
if treeDIA < 50:
    print("Cant cut")
else:
    print("Can")