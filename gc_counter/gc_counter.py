from Bio import SeqIO
from collections import defaultdict
from itertools import product




def process(path):
    file=SeqIO.parse(path, "fasta")

    result = []
    for i in file:
        seq = str(i.seq)
        result.append((seq.count("A")+seq.count("a"), (seq.count("C")+seq.count("c")), (seq.count("G")+seq.count("g")), (seq.count("T")+seq.count("t"))))
    return result
