import pandas as pd
import random
import numpy as np

class QlearningAgent(object):
    def __init__(self):
        self.epsilon = 0.2
        self.gamma = 0.9
        self.lr = 0.1


        self.last_s = None
        self.last_a = None
        try:
            #s, a, q
            self.table = np.genfromtxt('qtable.csv', dtype=np.float16, delimiter=',')
        except:
            print("initializing table")
            #state: 8 inputs condensed to int
            self.table = np.zeros((6561, 3), dtype=np.float16)
        
    def step(self, state, reward):
        if self.last_s is not None:
            self.update(self.last_s, self.last_a, state, reward)
        
        if random.uniform(0, 1) < self.epsilon:
            move = random.randint(-1, 1)
        else:
            options = self.table[state]
            move = random.choice(np.argmax(options)) - 1
            
        self.last_s = state
        self.last_a = move
        
    def update(self, s, a, ns, r):
          self.table[s, a] = self.table[s, a] + self.lr * (r + self.gamma * np.max(self.table[ns, :]) - self.table[s, a])
    
    def close(self, next_state, reward):

        pd.DataFrame(self.table).to_csv('qtable.csv')
        