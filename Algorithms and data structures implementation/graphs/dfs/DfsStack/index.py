from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        visited = set()
        st = []
        st.append(startNode)

        while(len(st)):
            cur = st[-1]
            st.pop()

            if(cur not in visited):
                print(cur, end=" ")
                visited.add(cur)

            for vertex in self.graph[cur]:
                if(vertex not in visited):
                    st.append(vertex)


g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)


g.DFS(2)
