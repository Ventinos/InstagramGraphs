import pickle

def serializeStructure(structure):
    filename = input('[Required] - Write the name of the new structure file: ')
    file = open(filename, 'wb')
    pickle.dump(structure, file)


def serializeStructure2(structure, filename):
    file = open(filename, 'wb')
    pickle.dump(structure, file)


def deserializeStructure():
    filename = input('[Required] - Write the name of the file: ')
    file = open(filename, 'rb')
    structure = pickle.load(file)
    return structure


def deserializeStructure2(filename):
    file = open(filename, 'rb')
    structure = pickle.load(file)
    return structure

