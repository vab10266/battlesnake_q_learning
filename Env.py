import numpy as np

class Env():
    def data_to_state(data):

        width = data['board']['width']
        height = data['board']['height']

        head_x = data['board']['you']['head']['x']
        head_y = data['board']['you']['head']['y']

        last_x = data['board']['you']['body'][1]['x']
        last_y = data['board']['you']['body'][1]['y']

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
                obstacles[k] = [obs_x, obs_y]
                k += 1

        #list food
        food = np.zeros((len(data['board']['food']), 2))
        for i in range(len(data['board']['food']):
          food_x = data['board']['food'][i]['x']
          food_y = data['board']['food'][i]['y']
          food[i] = [food_x, food_y]

        """
        --0--
        -123-
        45h67
        """

        if last_move == 0:
          sensor_locs = np.array([
            [head_x, head_y + 2],
            [head_x - 1, head_y + 1],
            [head_x, head_y + 1],
            [head_x + 1, head_y + 1],
            [head_x - 2, head_y],
            [head_x - 1, head_y],
            [head_x + 1, head_y],
            [head_x + 2, head_y]
          ])
        elif last_move == 1:
          sensor_locs = np.array([
            [head_x - 2, head_y],
            [head_x - 1, head_y - 1],
            [head_x - 1, head_y],
            [head_x - 1, head_y + 1],
            [head_x, head_y - 2],
            [head_x, head_y - 1],
            [head_x, head_y + 1],
            [head_x, head_y + 2]
          ])
        elif last_move == 2:
          sensor_locs = np.array([
            [head_x, head_y - 2],
            [head_x + 1, head_y - 1],
            [head_x, head_y - 1],
            [head_x - 1, head_y - 1],
            [head_x + 2, head_y],
            [head_x + 1, head_y],
            [head_x - 1, head_y],
            [head_x - 2, head_y]
          ])
        else: # last_move == 3:
          sensor_locs = np.array([
            [head_x + 2, head_y],
            [head_x + 1, head_y + 1],
            [head_x + 1, head_y],
            [head_x + 1, head_y - 1],
            [head_x, head_y + 2],
            [head_x, head_y + 1],
            [head_x, head_y - 1],
            [head_x, head_y - 2]
          ])


        sensor = np.zeros(8)

        for i in range():
          if (food == sensor_locs[i]).all(1).any():
            sensor[i] = 1
          if (obstacles == sensor_locs[i]).all(1).any():
            sensor[i] = -1
          if not (
            sensor_locs[i][0] >= 0 and
            sensor_locs[i][0] < width and
            sensor_locs[i][1] >= 0 and
            sensor_locs[i][1] < height
          ):
            sensor[i] = -1
        return state, last_move