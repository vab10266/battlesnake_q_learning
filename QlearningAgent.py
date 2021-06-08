import pandas as pd
import random

class QlearningAgent(object):
    def __init__(self):
        self.epsilon = 0.2
        self.lr = 0.9

        self.last_s = None
        self.last_a = None
        try:
            #s, a, q
            self.table = pd.read_csv('qtable.csv')
        finally:
            self.table = pd.DataFrame()
        
    def move(state):
        return 0
    
    def close(self, next_state, reward):

        self.table.to_csv('qtable.csv')
        