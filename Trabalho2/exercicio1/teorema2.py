from pygraph.classes.graph import graph
from pygraph.algorithms.accessibility import connected_components

def teo_2(g, k):
  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')
  if k <= 0:
    raise ValueError('FORBIDDEN: K <= 0')

  # Caso base
  if k == 1:
    forest = graph()
    for node in g.nodes():
      forest.add_node(node)
    return forest

  # Passo indutivo
  forest = teo_2(g, k-1)

  while True:
    cc = _transform_cc(connected_components(forest))
    
    selected_component = None
    for component in cc:
      if len(component) < k:
        selected_component = component
        break

    if selected_component == None:
      break

    edges = g.edges()
    used_edges = forest.edges()
    unused_edges = [e for e in edges if e not in used_edges]
    neighbor_edges = [e for e in unused_edges if e[0] in selected_component]

    min_edge = min(neighbor_edges, key=lambda e: g.edge_weight(e))
    forest.add_edge(min_edge)

  return forest


def _transform_cc(cc):
  inv_map = {}
  for k, v in cc.iteritems():
    inv_map[v] = inv_map.get(v, [])
    inv_map[v].append(k)
  return inv_map.values()


if __name__ == '__main__':
       
  import tsp_reader
  import sys
  from time import time

  EXECS_PER_LOOP = 1
  TIME_THRESHOLD = 5

  k = int(sys.argv[1])
  tsp_file = sys.argv[2]
  tsp_str = open(tsp_file).read()
  g = tsp_reader.read(tsp_str)

  if k == -1:
    k = len(g.nodes())

  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')

  start = time()
  execs = 0
  while time() - start < TIME_THRESHOLD:
      execs += EXECS_PER_LOOP
      for i in range(EXECS_PER_LOOP):
          f = teo_2(g, k)
  end = time()
  elapsed = end - start

  print("k = %d" % k)
  print("file = %s" % tsp_file)
  print("time/exec = %.6f ms" % (1000*elapsed/execs))
