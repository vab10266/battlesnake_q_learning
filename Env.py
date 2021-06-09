import numpy as np

class Env():
    def data_to_state(data):

        this_ind = 0
        for i in range(len(data['board']['snakes'])):
          if data['board']['snakes'][i]['name'] == "Vaud's first baby snake":
            this_ind = i
        
        head_x = data['you']['head']['x']
        head_y = data['you']['head']['y']

        last_x = data['you']['body'][1]['x']
        last_y = data['you']['body'][1]['y']

        last_move = 0
        if last_x < head_x:
          last_move = 3
        if last_x > head_x:
          last_move = 1
        if last_y > head_y:
          last_move = 2
        #["up", "left", "down", "right"]


        #list obstacles
        count = 0
        for i in range(len(data['board']['snakes'])):
            count += len(data['board']['snakes'][i]['body'])
        
        obstacles = np.zeros((count, 2))

        k = 0
        for i in range(len(data['board']['snakes'])):
            for j in range(len(data['board']['snakes'][i])):
                obs_x = data['board']['snakes'][i]['body'][j]['x']
                obs_y = data['board']['snakes'][i]['body'][j]['y']
                obstacles[k] = [obs_x][obs_y]
                k += 1
        
        #list food

        """
        --0--
        -123-
        45h67
        """
        sensors = np.zeros(8)
        if last_move == 0:

        return state, last_move