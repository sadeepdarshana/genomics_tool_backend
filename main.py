from mapper import mapper_search
from taxonomy import taxonomy
from blast import blast
from vectorizer import vectorizer
from gc_counter import gc_counter
from autoencoder import autoencoder

def process(input_fasta_path, k, epochs, activation, layers_sizes, train_perc):
    vectors = vectorizer.process(input_fasta_path, k)
    gc_contents = gc_counter.process(input_fasta_path)
    lineages = taxonomy.process(mapper_search.process(blast.process(input_fasta_path)))
    autoencoder_points = autoencoder.process(vectors, epochs, activation, layers_sizes, train_perc)
    return vectors, gc_contents, lineages, autoencoder_points