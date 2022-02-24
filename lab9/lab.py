"""6.009 Fall 2019 Lab 9 -- 6.009 Zoo"""

from math import acos
# NO OTHER IMPORTS ALLOWED!

class Constants:
    """
    A collection of game-specific constants.

    You can experiment with tweaking these constants, but
    remember to revert the changes when running the test suite!
    """
    # width and height of keepers
    KEEPER_WIDTH = 30
    KEEPER_HEIGHT = 30

    # width and height of animals
    ANIMAL_WIDTH = 30
    ANIMAL_HEIGHT = 30

    # width and height of food
    FOOD_WIDTH = 10
    FOOD_HEIGHT = 10

    # width and height of rocks
    ROCK_WIDTH = 50
    ROCK_HEIGHT = 50

    # thickness of the path
    PATH_THICKNESS = 30

    TEXTURES = {
        'rock': '1f5ff',
        'animal': '1f418',
        'SpeedyZookeeper': '1f472',
        'ThriftyZookeeper': '1f46e',
        'CheeryZookeeper': '1f477',
        'food': '1f34e'
    }

    FORMATION_INFO = {'SpeedyZookeeper':
                       {'price': 9,
                        'interval': 55,
                        'throw_speed_mag': 20},
                      'ThriftyZookeeper':
                       {'price': 7,
                        'interval': 45,
                        'throw_speed_mag': 7},
                      'CheeryZookeeper':
                       {'price': 10,
                        'interval': 35,
                        'throw_speed_mag': 2}}

class NotEnoughMoneyError(Exception):
    """A custom exception to be used when insufficient funds are available
    to hire new zookeepers. You may leave this class as is."""
    pass


################################################################################
################################################################################

class Game:
    def __init__(self, game_info):
        """Initializes the game.

        `game_info` is a dictionary formatted in the following manner:
          { 'width': The width of the game grid, in an integer (i.e. number of pixels).
            'height': The height of the game grid, in an integer (i.e. number of pixels).
            'rocks': The set of tuple rock coordinates.
            'path_corners': An ordered list of coordinate tuples. The first
                            coordinate is the starting point of the path, the
                            last point is the end point (both of which lie on
                            the edges of the gameboard), and the other points
                            are corner ("turning") points on the path.
            'money': The money balance with which the player begins.
            'spawn_interval': The interval (in timesteps) for spawning animals
                              to the game.
            'animal_speed': The magnitude of the speed at which the animals move
                            along the path, in units of grid distance traversed
                            per timestep.
            'num_allowed_unfed': The number of animals allowed to finish the
                                 path unfed before the player loses.
          }
        """
        self.width = game_info['width']
        self.height = game_info['height']
        self.rocks = set()
        for rock_loc in game_info['rocks']:
            rock = Rock(rock_loc)
            self.rocks.add(rock)
        self.path = [Vector(loc) for loc in game_info['path_corners']]
        self.money = game_info['money']
        self.spawn_interval = game_info['spawn_interval']
        self.animal_speed = game_info['animal_speed']
        self.num_allowed_remaining = game_info['num_allowed_unfed']
        self.animals = set()
        self.food = set()
        self.zookeepers = set()
        self.last_click = None
        self.status = 'ongoing'
        self.t = 0

    def formations(self):
        return list(self.rocks) + list(self.food) + list(self.zookeepers) + list(self.animals)

    def render(self):
        """Renders the game in a form that can be parsed by the UI.

        Returns a dictionary of the following form:
          { 'formations': A list of dictionaries in any order, each one
                          representing a formation. The list should contain
                          the formations of all animals, zookeepers, rocks,
                          and food. Each dictionary has the key/value pairs:
                             'loc': (x, y),
                             'texture': texture,
                             'size': (width, height)
                          where `(x, y)` is the center coordinate of the
                          formation, `texture` is its texture, and `width`
                          and `height` are its dimensions. Zookeeper
                          formations have an additional key, 'aim_dir',
                          which is None if the keeper has not been aimed, or a
                          tuple `(aim_x, aim_y)` representing a unit vector
                          pointing in the aimed direction.
            'money': The amount of money the player has available.
            'status': The current state of the game which can be 'ongoing' or 'defeat'.
            'num_allowed_remaining': The number of animals which are still
                                     allowed to exit the board before the game
                                     status is `'defeat'`.
          }
        """
        serial = {}
        formations = []
        for formation in self.formations():
            f = {}
            f['loc'] = (formation.loc.x, formation.loc.y)
            f['texture'] = formation.texture
            f['size'] = formation.size
            if isinstance(formation, Zookeeper):
                try:
                    f['aim_dir'] = (formation.aim.x, formation.aim.y)
                except:
                    f['aim_dir'] = None
            formations.append(f)
        serial['formations'] = formations
        serial['money'] = self.money
        serial['status'] = self.status
        serial['num_allowed_remaining'] = self.num_allowed_remaining
        # print(serial)
        return serial

    def out_of_bounds(self, formation):
        x = formation.loc.x
        y = formation.loc.y
        if x < 0 or x > self.width:
            return True
        if y < 0 or y > self.height:
            return True
        return False

    def move_formations(self):
        unfed = 0
        out = set()
        for animal in self.animals:
            animal.update_loc(self.path)
            if self.out_of_bounds(animal):
                out.add(animal)
                unfed += 1
        self.animals -= out
        out = set()
        for apple in self.food:
            apple.update_loc()
            if self.out_of_bounds(apple):
                out.add(apple)
        self.food -= out
        return unfed

    def feed(self):
        fed = set()
        eaten = set()
        for animal in self.animals:
            for apple in self.food:
                if animal.overlaps(apple):
                    fed.add(animal)
                    eaten.add(apple)
        self.animals -= fed
        self.food -= eaten
        return len(fed)

    def spawn_animal(self):
        if self.t % self.spawn_interval == 0:
            elephant = Animal(self.animal_speed, self.path)
            self.animals.add(elephant)

    def animal_in_sight(self, keeper):
        for animal in self.animals:
            u = keeper.aim.x
            v = keeper.aim.y
            ortho = Vector((-v,u))
            c = ortho.dot(keeper.loc)
            w = Constants.ANIMAL_WIDTH
            h = Constants.ANIMAL_HEIGHT
            directions = [Vector((-w/2,-h/2)), Vector((-w/2,h/2)), Vector((w/2,h/2)), Vector((w/2,-h/2))]
            corners = [animal.loc + dir for dir in directions]
            if any(ortho.dot(corner) > c for corner in corners) and any(ortho.dot(corner) < c for corner in corners):
                    if any(keeper.aim.dot(corner - keeper.loc) > 0 for corner in corners):
                        return True
        return False


    def throw_food(self):
        for keeper in self.zookeepers:
            if isinstance(keeper.aim, Vector):
                if (self.t - keeper.start_time) % keeper.interval == 0:
                    if self.animal_in_sight(keeper):
                        apple = Food(keeper.loc, keeper.aim, keeper.speed)
                        self.food.add(apple)

    def not_in_path(self, loc):
        u = loc.x
        v = loc.y
        for i in range(len(self.path)-1):
            x_0 = self.path[i].x
            y_0 = self.path[i].y
            x_1 = self.path[i+1].x
            y_1 = self.path[i+1].y
            if 2*abs(x_0-u) < Constants.KEEPER_WIDTH + Constants.PATH_THICKNESS:
                if x_0 == x_1:
                    if (v-(min(y_0,y_1)-Constants.PATH_THICKNESS))*(v-(max(y_0,y_1)+Constants.PATH_THICKNESS)) < 0:
                        return False
            if 2*abs(y_0-v) < Constants.KEEPER_WIDTH + Constants.PATH_THICKNESS:
                if y_0 == y_1:
                    if (u-(min(x_0,x_1)-Constants.PATH_THICKNESS))*(u-(max(x_0,x_1) + Constants.PATH_THICKNESS)) < 0:
                        return False
        return True

    def not_on_rock(self, loc):
        u = loc.x
        v = loc.y
        for rock in self.rocks:
            if 2*abs(rock.loc.x - u) < Constants.ROCK_WIDTH + Constants.KEEPER_WIDTH and 2*abs(rock.loc.y - v) < Constants.ROCK_HEIGHT + Constants.KEEPER_HEIGHT:
                return False
        return True

    def is_valid_loc(self, tuple):
        if self.not_in_path(tuple) and self.not_on_rock(tuple):
                return True
        return False

    def handle_mouse_input(self, mouse):
        if isinstance(self.last_click, Zookeeper):
            if Vector(mouse) != self.last_click.loc:
                aim = Vector(mouse)
                self.last_click.update_aim(aim)
                self.last_click = None
                return None
        else:
            if isinstance(mouse, str):
                self.last_click = mouse
            elif isinstance(mouse, tuple) and self.last_click != None:
                if self.money >= Constants.FORMATION_INFO[self.last_click]['price']:
                    pass
                else:
                    raise NotEnoughMoneyError
                if self.last_click != None:
                    loc = Vector(mouse)
                    if self.is_valid_loc(loc):
                        keeper = Zookeeper(loc, self.last_click, self.t)
                        self.zookeepers.add(keeper)
                        self.money -= Constants.FORMATION_INFO[self.last_click]['price']
                        self.last_click = keeper


    def timestep(self, mouse=None):
        """Simulates the evolution of the game by one timestep.

        In this order:
            (0. Do not take any action if the player is already defeated.)
            1. Compute any changes in formation locations, then remove any
                off-board formations.
            2. Handle any food-animal collisions, and remove the fed animals
                and eaten food.
            3. Throw new food if possible.
            4. Spawn a new animal from the path's start if needed.
            5. Handle mouse input, which is the integer coordinate of a player's
               click, the string label of a particular zookeeper type, or `None`.
            6. Redeem one unit money per animal fed this timestep.
            7. Check for the losing condition to update the game status if needed.
        """
        ### 0.
        if self.status == 'ongoing':
            ### 1.
            unfed = self.move_formations()
            ### 2.
            num_fed = self.feed()
            ### 3.
            self.throw_food()
            ### 4.
            self.spawn_animal()
            ### 5.
            if mouse != None:
                self.handle_mouse_input(mouse)
            ### 6.
            self.money += num_fed
            ### 7.
            self.num_allowed_remaining -= unfed
            if self.num_allowed_remaining < 0:
                self.status = 'defeat'
        self.t += 1




################################################################################
################################################################################
# TODO: Add a Formation class and at least two additional classes here.
class Formation():
    def __init__(self, location, texture, size):
        '''
        '''
        if isinstance(location, tuple):
            location = Vector(location)
        self.loc = location
        self.texture = texture
        self.size = size

    def overlaps(self, other):
        d = self.loc - other.loc
        x = abs(d.x)
        y = abs(d.y)
        if 2*x < (self.size[0] + other.size[0]) and 2*y < (self.size[1] + other.size[1]):
            return True
        return False

class Animal(Formation):
    def __init__(self, speed, path):
        '''
        '''
        super().__init__(path[0],Constants.TEXTURES['animal'],(Constants.ANIMAL_WIDTH, Constants.ANIMAL_HEIGHT))
        self.speed = speed
        self.corner = 0

    def __str__(self):
        return 'Animal at ' + str((self.loc.x,self.loc.y))

    def update_loc(self, path, distance_to_travel=None):
        if distance_to_travel == None:
            distance_to_travel = self.speed
        try:
            next_corner = path[self.corner+1]
            dir = (next_corner - self.loc) / abs(next_corner - self.loc)
            distance_remaining = abs(next_corner - self.loc)
            if distance_remaining > distance_to_travel:
                self.loc = (distance_to_travel * dir) + self.loc
            else:
                self.loc = next_corner
                self.corner += 1
                self.update_loc(path, distance_to_travel-distance_remaining)
        except:
            dir = path[-1] - path[-2]
            self.loc += distance_to_travel * dir

class Food(Formation):
    def __init__(self, location, aim, speed):
        '''
        '''
        super().__init__(location, Constants.TEXTURES['food'], (Constants.FOOD_WIDTH,Constants.FOOD_HEIGHT))
        self.aim = aim
        self.speed = speed

    def update_loc(self):
        self.loc += self.speed * self.aim

class Zookeeper(Formation):
    def __init__(self, location, type, time):
        '''
        '''
        super().__init__(location, Constants.TEXTURES[type], (Constants.KEEPER_WIDTH,Constants.KEEPER_HEIGHT))
        self.start_time = time + 1
        self.interval = Constants.FORMATION_INFO[type]['interval']
        self.speed = Constants.FORMATION_INFO[type]['throw_speed_mag']
        self.aim = None

    def update_aim(self, aim):
        self.aim = (aim-self.loc)/abs(aim-self.loc)

class Rock(Formation):
    def __init__(self, location):
        '''
        '''
        super().__init__(location, Constants.TEXTURES['rock'], (Constants.ROCK_WIDTH,Constants.ROCK_HEIGHT))

    def __str__(self):
        return 'Rock at ' + str((self.loc.x,self.loc.y))


class Vector():
    def __init__(self, coordinates):
        x,y = coordinates
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __ne__(self,other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Vector((self.x+other.x,self.y+other.y))

    def __sub__(self, other):
        return Vector((self.x-other.x,self.y-other.y))

    def __abs__(self):
        return (self.x**2 + self.y**2) ** (1/2)

    def __rmul__(self, other):
        return Vector((self.x*other,self.y*other))

    def __truediv__(self, other):
        return Vector((self.x/other,self.y/other))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

################################################################################
################################################################################



if __name__ == '__main__':
   pass
