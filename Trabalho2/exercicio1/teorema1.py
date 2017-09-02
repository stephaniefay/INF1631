from pygraph.classes.graph import graph

def teo_1(g, k):
  if k > len(g.nodes()):
    raise ValueError('FORBIDDEN: K > |V|')
  if k <= 0:
    raise ValueError('FORBIDDEN: K <= 0')

  # Caso base
  if k == 1:
    tree = graph()
    tree.add_node(1)
    return tree

  # Hipotese indutiva
  tree = teo_1(g, k-1)

  all_nodes = g.nodes()
  used_nodes = tree.nodes()
  external_nodes = [node for node in all_nodes if node not in used_nodes]

  r = []
  for used_node in used_nodes:
    for external_node in external_nodes:
      if g.has_edge((used_node, external_node)):
        r.append((used_node, external_node))

  new_edge = max(r, key=lambda e: g.edge_weight(e))

  a, b = new_edge
  tree.add_node(b)

  tree.add_edge(new_edge)

  return tree

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
          f = teo_1(g, k)
  end = time()
  elapsed = end - start

  print("k = %d" % k)
  print("file = %s" % tsp_file)
  print("time/exec = %.6f ms" % (1000*elapsed/execs))
