import networkx as nx
from networkx.algorithms import bipartite
import matplotlib as mpl
import matplotlib.pyplot as plt

B = nx.Graph()

def addNodes():
    B.add_nodes_from(['u1','u2','u3','u4', 'u4'], bipartite='user')
    B.add_nodes_from(['Cold','Hot'], bipartite='item')

    B.add_weighted_edges_from([('u1','Cold',1),('u1','Hot',0.75),('u3','Cold',1.2),('u2','Hot',0.375), ('u4','Hot',0.8), ('u5','Hot',0.9)])
    '''
    B.add_edge('u1','Cold',weight=1)
    B.add_edge('u1','Hot',weight=0.7)
    B.add_edge('u2','Cold',weight=0.1)
    B.add_edge('u2','Hot',weight=1)
    B.add_edge('u3','Cold',weight=0.8)
    B.add_edge('u4','Hot',weight=1)
    B.add_edge('u5','Hot',weight=1)
    '''
    X = ['u1','u2','u3','u4', 'u5']
    Y = ['Cold', 'Hot']
    return B, X, Y

def drawNetWork(B, Components, Proprty):
    #区域就算了 搞了一下午还是没捣鼓出来怎么画
    X = Components
    Y = Proprty
    #Z = ['Hot']

    Edges = []
    pos = dict()
    pos.update( (n, (1, i+0.5)) for i, n in enumerate(X) )
    pos.update( (n, (2, i+1.5)) for i, n in enumerate(Y) )
    nx.draw_networkx_nodes(B, pos, nodelist=X, node_color='slategray',alpha=0.95, node_size = 400)
    nx.draw_networkx_nodes(B, pos, nodelist=Y, node_color='steelblue',alpha=0.95, node_size = 400)
    nx.draw_networkx_labels(B,pos)

    colors = [ B.edges[u,i]['weight'] for u,i in B.edges]
    edges = nx.draw_networkx_edges(B, pos = pos, edge_color = colors,
            width=3, edge_cmap=plt.cm.Blues, edge_vmin =0, alpha=0.9)

    pc = mpl.collections.PatchCollection(Edges, cmap=plt.cm.Blues)
    pc.set_array(colors)
    plt.colorbar(pc)
    ax = plt.gca()
    ax.set_axis_off()

    plt.show()
    
if __name__ == '__main__':
    B, X, Y = addNodes()
    drawNetWork(B, X, Y)
