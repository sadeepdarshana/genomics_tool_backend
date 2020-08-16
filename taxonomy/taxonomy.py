
data_path = './taxonomy/data/rankedlineage.dmp'

file = open(data_path, encoding='utf-8')

lineage = None

def load_to_memory():
    global lineage
    if lineage is not None: return
    lineage = {}
    i=0
    for line in file:
        i += 1
        line_components = [i.replace('\t', '').strip() for i in line.split('|')]
        lineage[int(line_components[0])] = line_components[2:-1]


def process(data):
    load_to_memory()
    return [lineage[x] if x in lineage else None for x in data]


