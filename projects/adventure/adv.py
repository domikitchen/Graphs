from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        
        else:
            return None

    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        
        else:
            return None
    
    def size(self):
        return len(self.queue)

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def go():
    stack = Stack()

    visited = set()

    while len(visited) < len(world.rooms):
        path = []

        for exits in player.current_room.get_exits():
            if player.current_room.get_room_in_direction(exits) not in visited:
                path.append(exits)

        if player.current_room not in visited:
            visited.add(player.current_room)

        if len(path) > 0:
            random_path_movement = random.randint(0, len(path) - 1)

            stack.push(path[random_path_movement])
            player.travel(path[random_path_movement])

            traversal_path.append(path[random_path_movement])

        else:
            last = stack.pop()
            if last == "n":
                player.travel("s")
                traversal_path.append("s")
            elif last == "s":
                player.travel("n")
                traversal_path.append("n")
            elif last == "w":
                player.travel("e")
                traversal_path.append("e")
            elif last == "e":
                player.travel("w")
                traversal_path.append("w")
            else:
                print("heck <_<")

go()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

