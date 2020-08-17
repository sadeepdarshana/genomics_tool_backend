from Bio import SeqIO
import pandas as pd

def process(path):
    file=SeqIO.parse(path, "fasta")

    sequences = []
    for i in file:
        sequences.append(str(i.seq))
    return pd.DataFrame(sequences, columns=['sequence'])
