import os


def ReadFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("File does not exists")
    infile = open(filename, "r")
    line = infile.readline()
    return line
