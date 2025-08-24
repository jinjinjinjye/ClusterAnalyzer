import numpy as np
from collections import deque

# TODO: verify
# TODO: unit tests, visualization
# TODO: random value seed for reproducibility? 

def la_fifo(L, p, seed=None):
    """
    Leath–Alexandrowicz FIFO algorithm for site percolation on a square lattice.
    
    Parameters
    ----------
    L : int
        Linear size of the lattice (LxL).
    p : float
        Occupation probability (0 <= p <= 1).
    seed : tuple or None
        Starting seed site (i, j). If None, defaults to center of lattice.
    
    Returns
    -------
    cluster : set of tuple
        Coordinates of occupied sites belonging to the grown cluster.
    """
    # Lattice state: -1 = unvisited, 0 = empty, 1 = occupied
    state = -np.ones((L, L), dtype=int)
    
    if seed is None:
        seed = (L // 2, L // 2)
    
    cluster = set()
    q = deque([seed])
    state[seed] = 1
    cluster.add(seed)

    while q:
        x, y = q.popleft()
        
        # Nearest neighbors (von Neumann)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < L and 0 <= ny < L:
                if state[nx, ny] == -1:  # unvisited
                    if np.random.rand() < p:
                        state[nx, ny] = 1
                        cluster.add((nx, ny))
                        q.append((nx, ny))
                    else:
                        state[nx, ny] = 0  # permanently empty
    
    return cluster

# TODO
def la_lifo(L, p, seed=None):
  
  
  if seed is None:
      seed = (L // 2, L // 2)

  
  cluster = set()

return cluster
  
