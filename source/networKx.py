import matplotlib.pyplot as plt
import networkx as nx
import sqlite3
import collections
# ================================sqlite================================
def koneksi(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None
def ambilNode(conn):
    node = set()
    
    cur = conn.cursor()
    cur.execute("select DISTINCT link_keluar from data")
    rows = cur.fetchall()
    for row in rows:
        tmp = str(row[0])
        node.add(tmp)
    
    cur = conn.cursor()
    cur.execute("select DISTINCT url from data")
    rows = cur.fetchall()
    for row in rows:
        tmp = str(row[0])
        node.add(tmp)
    
    return node
def ambilEdge(conn):
    kumpulanEdge = list()
    primNode = list()
    
    cur = conn.cursor()
    cur.execute("select DISTINCT url from data")
    rows = cur.fetchall()
    for row in rows:
        
        tmp = str(row[0])
        primNode.append(tmp)
    
    for x in primNode:
        edge = list()
        cur = conn.cursor()
        query =  "select link_keluar from data where url='"+str(x)+"'"

        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            tmp =[str(x),str(row[0])] 
            edge.append(tmp)
        kumpulanEdge.append(edge)
    return kumpulanEdge
    
# ================================graph================================

# ================================main================================
def main(): 
    graph=nx.Graph()
    node = set()
    database = "data.sqlite"
    conn = koneksi(database)
    with conn: 
        node = ambilNode(conn)
        kumpulanEdge = ambilEdge(conn)
    graph.add_nodes_from(node)
    for x in kumpulanEdge :
        # print("===== edge =====" , kumpulanEdge[x])
        graph.add_edges_from(x)
    pr =  nx.pagerank(graph)
    # print(pr)
    # print(type(pr))  
    sorted_pr = sorted(pr.items() , reverse = True, key=lambda kv: kv[1])
    print("========== Top 3 pagerank ==========")
    print("1. ", sorted_pr[0])
    print("2. ", sorted_pr[1])
    print("3. ", sorted_pr[2])
    nx.draw(graph)
    plt.show()
if __name__ == '__main__':
	main()
