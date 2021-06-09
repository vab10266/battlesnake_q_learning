import os
import random
import Env
import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""

class Battlesnake(object):
    def __init__(self):
      super.__init__()
      self.agents = {}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "vab10266",  # TODO: Your Battlesnake Username
            "color": "#ff0000",  # TODO: Personalize
            "head": "sand-worm",  # TODO: Personalize
            "tail": "weight",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        self.agents[data['game']['id']] = QlearningAgent()

        print("START")
        import sys

        print('This message will be displayed on the screen.')

        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json
        print(f"DATA: {data}")

        state, last_move, sensor = Env.data_to_state(data)

        log(state)
        log(last_move)
        log(" - - " + str(sensor[0]) + " - - \n"
            + " - " + str(sensor[1]) + " " + str(sensor[2]) + " " +  + str(sensor[3]) + " - \n"
            + str(sensor[4]) + " " + str(sensor[5]) + " h " + str(sensor[6]) + " " + str(sensor[7]) + " "
        )

        agent = self.agents[data['game']['id']]

        action = agent.step(state, 0.01)

        move = Env.action_to_move(action, last_move)
        return move

        '''
        this_ind = 0
        for i in range(len(data['board']['snakes'])):
          if data['board']['snakes'][i]['name'] == "Vaud's first baby snake":
            this_ind = i

        head_x = data['board']['snakes'][this_ind]['head']['x']
        head_y = data['board']['snakes'][this_ind]['head']['y']

        last_x = data['board']['snakes'][this_ind]['body'][1]['x']
        last_y = data['board']['snakes'][this_ind]['body'][1]['y']

        last_move = 0
        if last_x < head_x:
          last_move = 3
        if last_x > head_x:
          last_move = 1
        if last_y > head_y:
          last_move = 2

        # Choose a random direction to move in
        possible_moves = ["up", "left", "down", "right"]
        available_moves = ["up", "left", "down", "right"]

        available_moves.pop((last_move - 2)%4)

        #move = random.choice(possible_moves)
        #move = possible_moves[data['turn']%4]

        if head_x == data['board']['width'] - 1 and "right" in available_moves:
          available_moves.remove("right")
        if head_y == data['board']['height'] - 1 and "up" in available_moves:
          available_moves.remove("up")
        if head_x == 0 and "left" in available_moves:
          available_moves.remove("left")
        if head_y == 0 and "down" in available_moves:
          available_moves.remove("down")

        move = random.choice(available_moves)
        print(f"MOVE: {move}")
        log(move)
        print(data['game'])
        return {"move": move}
        '''


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json
        reward = 0
        if len(data['board']['snakes']) == 1 and data['board']['snakes'][0]['id'] == data['board']['you']['id']:
          reward = 1

        state, last_move, sensor = Env.data_to_state(data)

        self.agents[data['game']['id']].close(state, reward)

        self.agents.remove(data['game']['id'])

        print("END")
        return "ok"

def log(msg):
  with open('log.txt', 'a') as f:
    print(msg, "\n", file=f)



if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
