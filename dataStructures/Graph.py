class Graph:

  def __init__(self):
    self.adj_list = {}
  
  def print_graph(self):
    v_list = []
    for vertex in self.adj_list:
      v_list.append(vertex)
    v_list.sort()
    for v in v_list:
      print(v, ':', self.adj_list[v])
  
  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = []
      return True
    return False
  
  def add_edge(self, v1, v2):
    if v1 in self.adj_list and v2 in self.adj_list:
      self.adj_list[v1].append(v2)
      self.adj_list[v2].append(v1)
      return True
    return False
  
  def add_edges(self):
    for i in self.adj_list:
      for j in self.adj_list:
        if i != j and i in self.adj_list and j in self.adj_list:
            self.adj_list[i].append(j)

  def add_edge2(self):
    for i in range(len(self.adj_list)-1):
      self.add_edge(i, i+1)
  
  def remove_edge(self, v1, v2):
    if v1 in self.adj_list and v2 in self.adj_list: 
      try:
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)
      except ValueError:
        pass
      return True
    return False
  
  def remove_vertex(self, vertex):
    if vertex in self.adj_list:
      for other_vertex in self.adj_list[vertex]:
        self.adj_list[other_vertex].remove(vertex)
      del self.adj_list[vertex]
      return True
    return False