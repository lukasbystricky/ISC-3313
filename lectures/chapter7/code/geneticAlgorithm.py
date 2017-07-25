import numpy as np

def _initial_population(K=1000, xmin=-1, xmax=1, ymin=-1, ymax=1):
    # create a random array of K rows and 2 columns 
    population = np.random.rand(K, 2) 
    
    # scale from range (0,1)x(0,1) to (xmin,xmax)x(ymin,ymax)
    for k in range(K):
        population[k,0] = population[k,0]*(xmax-xmin) + xmin
        population[k,1] = population[k,1]*(ymax-ymin) + ymin
        
    return population
    

def _score_population(p, f):
    
    # plug every row of p into f
    scores = np.apply_along_axis(f, 1, p)
    scores = scores.reshape(len(scores),1)
    # sort scores
    
    # first append population as last two columns to score
    # matrix will now look like (x,y,score)
    scores = np.append(p, scores, 1)
    
    # sort by last column 
    scores = scores[scores[:,-1].argsort()]
    
    return scores
    
def _elite_children(p, n=2):
    
    # take elite children (no score)
    elite = p[0:n,0:-1]
    
    # remove from population
    p = np.delete(p, np.arange(0,n), 0)
    
    return elite, p
    
def _select_parents(scores, n = 0.25, M = 4):
    
    # compute number of parents
    N = int(n*len(scores))
    
    parents = []
    for i in range(N):
        
        # create pool of possible parents
        pool = []
        for j in range(M):
            r = np.random.randint(0,len(scores))
            pool.append(scores[r,:])
        
        # sort pool
        pool = np.array(pool)
        pool = pool[pool[:,-1].argsort()]
        
        # add individual with best score
        parents.append(pool[0,:])
        
    return np.array(parents)   

def _crossover_children(parents, N):
    
    children = []    
    for i in range(N):
        
        # create random binary vector
        r = np.array([np.random.randint(0,2),np.random.randint(0,2)])
        
        # choose 2 parents
        p1 = parents[np.random.randint(0,len(parents)), 0:2]
        p2 = parents[np.random.randint(0,len(parents)), 0:2]
        
        # get genes
        if r[0] == 0:
            g1 = p1[0]
        else:
            g1 = p2[0]
            
        if r[1] == 0:
            g2 = p1[1]
        else:
            g2 = p2[1]
            
        children.append(np.array([g1,g2]))
        
    return np.array(children)
    
def _mutation_children(parents, N, k, sigma0 = 2, G = 20):
    
    # compute standard deviation
    sigma = sigma0*(1 - k/G)
    
    children = []
    for i in range(N):
        r = np.random.randint(0,len(parents))
        
        g1 = parents[r,0] + sigma*np.random.randn()
        g2 = parents[r,1] + sigma*np.random.randn()
        
        children.append(np.array([g1,g2]))
        
    return np.array(children)
    
def ga(f, xmin, xmax, ymin, ymax, N, Gmax=20):
    
    population = []
    population.append(_initial_population(N, xmin,xmax,ymin,ymax))
    
    for k in range(Gmax):

        scores = _score_population(population[-1], f)
        elites, scores = _elite_children(scores)
        
        parents = _select_parents(scores)
        crossovers = _crossover_children(parents, int(0.8*N))
        mutations = _mutation_children(parents, int(0.2*N), k)
        
        # create next generation
        all_children = np.append(elites, crossovers, 0)
        all_children = np.append(all_children, mutations, 0)
        
        population.append(all_children)
        
    # sort final population by scores, extract best parameters
    scores = _score_population(population[-1], f)
    x_opt = scores[0,:-1]
    
    return population, x_opt
