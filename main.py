from mapper import mapper_search
from taxonomy import taxonomy
from blast import blast
from vectorizer import vectorizer
from gc_counter import gc_counter
from autoencoder import autoencoder
from reader import reader

def process(input_fasta_path, k, epochs, activation, layers_sizes, train_perc):
    data = reader.process(input_fasta_path)
    print('loaded input file')
    vectorizer.process(data, k)
    print('vectorizing done')
    gc_counter.process(data)
    print('gc count done')
    blast.process(data, input_fasta_path)
    print('blast done')
    mapper_search.process(data)
    print('mapping done')
    taxonomy.process(data)
    autoencoder.process(data, epochs, activation, layers_sizes, train_perc)
    data.drop('sequence', axis=1, inplace=True)
    data.drop('vector', axis=1, inplace=True)
    return data


def process_ae(input_fasta_path, k, epochs, activation, layers_sizes, train_perc, data):
    sequences = reader.process(input_fasta_path)
    data['sequence'] = sequences['sequence']
    print('loaded input file')
    vectorizer.process(data, k)
    print('vectorizing done')
    autoencoder.process(data, epochs, activation, layers_sizes, train_perc)
    data.drop('sequence', axis=1, inplace=True)
    data.drop('vector', axis=1, inplace=True)
    return data