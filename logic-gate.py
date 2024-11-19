def and_gate(a,b):
    return a and b


def or_gate(a,b):
    return a or b

def nand_gate(a,b):
    return not(a and b)

def nor_gate(a,b):
    return not(a or b)


def xor_gate(a,b):
    return (a and not b) or (not a and b)

def xnor_gate(a,b):o
    return not ((a and not b) or (not a and b))

print("\n=============================")
print("\n|by bayu from Loraine's lab|")
print("\n=============================")

print("         logic gate!")
print("\n=============================")

print("and gate")
print(and_gate(True,True))
print(and_gate(False,True))
print(and_gate(True,False))
print(and_gate(False,False))

print("\nor gate")
print(or_gate(True,True))
print(or_gate(False,True))
print(or_gate(True,False))
print(or_gate(False,False))

print("\nnand gate")
print(nand_gate(True,True))
print(nand_gate(False,True))
print(nand_gate(True,False))
print(nand_gate(False,False))

print("\nnor")
print(nor_gate(True,True))
print(nor_gate(False,True))
print(nor_gate(True,False))
print(nor_gate(False,False))

print("\nxor")
print(xor_gate(True,True))
print(xor_gate(False,True))
print(xor_gate(True,False))
print(xor_gate(False,False))

print("\nxnor")
print(xnor_gate(True,True))
print(xnor_gate(False,True))
print(xnor_gate(True,False))
print(xnor_gate(False,False))