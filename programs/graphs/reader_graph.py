from ..files.files import readFile

def readerGraph(configGraph):
    if configGraph['fromFile']:
        file = readFile('\\files\\graph\\graph.txt').split('\n')
        graph = list(file[i].split(',') for i in range(len(file)))
        print(graph)
        if len(graph[-1])==1 and graph[-1][0]=='':
            graph.pop()
        for row in graph:
            for j in row:
                int(j)
        return graph
    else:
        return configGraph['target']
