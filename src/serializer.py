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
    filename = f'bins/{filename}'
    file = open(filename, 'rb')
    structure = pickle.load(file)
    return structure

def deserializeStructure2(filename):
    file = open(filename, 'rb')
    structure = pickle.load(file)
    return structure

def deserializeStructurePath(path):
    with open(path,'rb') as file:
        structure = pickle.load(file)
    return structure

def serializeStructurePath(structure, path):
    with open(path, 'wb') as file:
        pickle.dump(structure, file)
        