import pandas as pd
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
        if lineage[int(line_components[0])][0] == '': lineage[int(line_components[0])][0] = line_components[1]


def process(data):
    load_to_memory()
    lineages =  [lineage[x] if x in lineage else ['']*8 for x in data['taxid']]

    for i in range(8):
        data['lin_'+str(i)] = pd.Series([lineages[x][i] for x in range(data.shape[0])])
