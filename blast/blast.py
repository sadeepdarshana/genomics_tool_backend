from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
from io import StringIO


blast_db = './blast/data/data.fasta'

def process(data):
    query_fasta_path = data

    blastn_results_xml = NcbiblastnCommandline(query=query_fasta_path, db=blast_db, outfmt=5)()
    blastn_results = NCBIXML.parse(StringIO(blastn_results_xml[0]))

    results_accessions = []
    for i in blastn_results:
        try:
            accession = i.alignments[0].accession
        except:
            accession = -1

        results_accessions.append(accession)

    return results_accessions
