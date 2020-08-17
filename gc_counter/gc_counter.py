from Bio import SeqIO
from collections import defaultdict
from itertools import product




def process(data):
    data['a'] = data['sequence'].map(lambda x: x.count("A")+x.count("a"))
    data['c'] = data['sequence'].map(lambda x: x.count("C")+x.count("c"))
    data['g'] = data['sequence'].map(lambda x: x.count("G")+x.count("g"))
    data['t'] = data['sequence'].map(lambda x: x.count("T")+x.count("t"))
