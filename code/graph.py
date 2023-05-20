from settings import VERTICAL_TILES, HORIZONTAL_TILES
import queue as Q

class Vertex:
    def __init__(self, x, y, object):
        self.x = x
        self.y = y
        self.distance = -1
        self.previous = None
        self.object = object

class Graph():
    def __init__(self, ground, objects):
        self.ground = ground
        self.objects = objects
        self.vertices = {}
        self.adjacency_dict = {}
        self.player_vertex = None
        self.chest_vertex = None

        self.create_verticies()
        self.create_adjacency_dict()
        self.find_objects()
  
    def create_verticies(self):
        not_vertices_tiles = ['51', '52', '53', '42']
        for x in range(HORIZONTAL_TILES):
            for y in range(VERTICAL_TILES):
                if self.ground[y][x] not in not_vertices_tiles:
                    index = str(x - 1) + "," + str(y - 1)
                    object_at_vertex = self.objects[y][x]
                    self.vertices[index] = Vertex(x - 1, y - 1, object_at_vertex)
    
    def create_adjacency_dict(self):
        adj_list = []
        for key, value in self.vertices.items():
            if value.object == '2':
                self.adjacency_dict[key] = [] 
                continue
            if (str(value.x + 1) + "," + str(value.y)) in self.vertices.keys():
                if self.vertices[str(value.x + 1) + "," + str(value.y)].object != '2':
                    adj_list.append(self.vertices[str(value.x + 1) + "," + str(value.y)])

            if (str(value.x - 1) + "," + str(value.y)) in self.vertices.keys():
                if self.vertices[str(value.x - 1) + "," + str(value.y)].object != '2':
                    adj_list.append(self.vertices[str(value.x - 1) + "," + str(value.y)])

            if (str(value.x) + "," + str(value.y + 1)) in self.vertices.keys():
                if self.vertices[str(value.x) + "," + str(value.y + 1)].object != '2':
                    adj_list.append(self.vertices[str(value.x) + "," + str(value.y + 1)])

            if (str(value.x) + "," + str(value.y - 1)) in self.vertices.keys():
                if self.vertices[str(value.x) + "," + str(value.y - 1)].object != '2':
                    adj_list.append(self.vertices[str(value.x) + "," + str(value.y - 1)])
                 
            self.adjacency_dict[key] = adj_list
            adj_list = []

    def find_objects(self):
        for key, value in self.vertices.items():
            if value.object == "0":
                self.player_vertex = value
            elif value.object == "1":
                self.chest_vertex = value
            if self.player_vertex is not None and self.chest_vertex is not None:
                return

    def BFS(self):
        self.player_vertex.distance = 0
        queue = Q.Queue()
        queue.put(self.player_vertex)
        while not queue.empty():
            u = queue.get()
            for vertex in self.adjacency_dict[str(u.x) + "," + str(u.y)]:
                if vertex.distance != -1:
                    continue
                vertex.distance = u.distance + 1
                vertex.previous = u
                queue.put(vertex)

    def get_path(self):
        if self.player_vertex == None or self.chest_vertex == None:
            return
        self.BFS()
        if self.chest_vertex.distance == -1:
            return
        current = self.chest_vertex
        path_list = [current]

        while current is not self.player_vertex:
            current = current.previous
            path_list.append(current)
        
        path_list.reverse()
        return path_list
