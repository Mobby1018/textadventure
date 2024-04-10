_world = {}
starting_position = (0, 0)

def load_tiles():
    with open('resources/map.csv', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[].split('/t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in rang(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(___import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))
