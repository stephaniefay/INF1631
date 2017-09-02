def teorema_3(costs, rewards, energy):
  if energy < 0:
    raise ValueError("Invalid energy!!")

  memory = {}

  memory[(0, 0)] = (0, [0])
  for y in range(1, 64):
    memory[(y, 0)] = None

  for x in range(1, energy+1):
    for y in range(64):
      nextCost = x - costs[y]
      vizinhos = find_neighbors(y)
      if nextCost < 0:
        memory[(y, x)] = None
      else:
        tuplas = [memory[(vizinho, nextCost)] for vizinho in vizinhos if not memory[(vizinho, nextCost)] == None]
        if len(tuplas) > 0:
          melhor_vizinho = max(tuplas, key=lambda x: x[0])
          novo_premio = melhor_vizinho[0] + rewards[y]
          novo_caminho = melhor_vizinho[1][:] + [y]
          memory[(y, x)] = (novo_premio, novo_caminho)
        else:
          memory[(y, x)] = None

  maior = 0
  for x in range(energy, -1, -1):
    x = memory[(0, x)]
    if x != None and x[0] > maior:
      maior = x[0]
      inst = x + (x,)
  return inst


def find_neighbors(pos):
  x = pos/8
  y = pos%8

  naive = [(x-1, y-1), (x-1, y), (x-1, y+1),
           (x,   y-1),           (x,   y+1),
           (x+1, y-1), (x+1, y), (x+1, y+1)]
  filtered = [n for n in naive if n[0]>=0 and n[1]>=0 and n[0]<8 and n[1]<8]

  return map(lambda pos: pos[0]*8+pos[1], filtered)



if __name__ == '__main__':

  import sys
  from time import time

  EXECS_PER_LOOP = 100
  TIME_THRESHOLD = 5

  problems = []
  with open('walk.in') as f:

    q = int(f.readline().strip())
    while q != 0:
      costs   = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])
      rewards = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])

      problems.append({'energy': q, 'costs': costs, 'rewards': rewards})

      q = int(f.readline().strip())

    for n, problem in enumerate(problems):
     start = time()
     execs = 0
     while time() - start < TIME_THRESHOLD:
         execs += EXECS_PER_LOOP
         for i in range(EXECS_PER_LOOP):
           solution = teorema_3(problem['costs'], problem['rewards'], problem['energy'])
     end = time()
     elapsed = end - start
     print("num = %d" % n)
     print("time/exec = %.6f ms" % (1000*elapsed/execs))
  
  for problem in problems:
    solution = teorema_3(problem['costs'], problem['rewards'], problem['energy'])
    print solution[0]
    print solution[2]
    print q
    print ' '.join(str(x) for x in solution[1])