import pickle

def serializeStructure(structure):
    filename = input('[Required] - Write the name of the new structure file: ')
    file = open(filename, 'wb')
    pickle.dump(structure, file)

def deserializeStructure():
    filename = input('[Required] - Write the name of the file: ')
    file = open(filename, 'rb')
    structure = pickle.load(file)
    return structure
