from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
from io import StringIO
import pandas as pd


blast_db = './blast/data/data.fasta'

def process(data, input_fasta_path):

    blastn_results_xml = NcbiblastnCommandline(query=input_fasta_path, db=blast_db, outfmt=5)()
    blastn_results = NCBIXML.parse(StringIO(blastn_results_xml[0]))

    results_accessions = []
    for i in blastn_results:
        try:
            accession = i.alignments[0].accession
        except:
            accession = -1

        results_accessions.append(accession)

    data['accession'] = pd.Series(results_accessions)
