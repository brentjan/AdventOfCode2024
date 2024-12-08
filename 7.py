TURN = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}
DX = {
    '^': 0,
    '>': 1,
    'v': 0,
    '<': -1
}
DY = {
    '^': -1,
    '>': 0,
    'v': 1,
    '<': 0
}

class World:
    def __init__(self, input_file="data/test.in"):
        self.world = []

        with open(input_file) as file:
            for line in file:
                self.world.append(line.rstrip())

        self.guard_states = ['^', '>', 'v', '<']
        self.nrows = len(self.world)
        self.ncols = len(self.world[0])
        self.x, self.y, self.guard = self.get_guard()
        self.path = {(self.x, self.y, self.guard)}
        self.extra_obstacle = None
        self.out_of_bound = False
        self.in_cycle = False


    def reset(self):
        self.x, self.y, self.guard = self.get_guard()
        self.path = {(self.x, self.y, self.guard)}
        self.extra_obstacle = None
        self.out_of_bound = False
        self.in_cycle = False


    def set_state(self, state):
        self.x, self.y, self.guard, self.path, self.extra_obstacle, self.out_of_bound, self.in_cycle = state


    def give_state(self):
        return self.x, self.y, self.guard, self.path, self.extra_obstacle, self.out_of_bound, self.in_cycle


    def is_inbound(self, x, y):
        return 0 <= x < self.ncols and 0 <= y < self.nrows


    def get_guard(self):
        x, y = 0, 0
        for x in range(self.ncols):
            for y in range(self.nrows):
                if self.world[y][x] in self.guard_states:
                    return x, y, self.world[y][x]
                
        raise LookupError("Guard not in world")
    

    def get_world_element(self, x, y):
        return self.world[y][x]
    

    def turn(self):
        self.guard = TURN[self.guard]


    def next_pos(self):
        new_x, new_y = self.x + DX[self.guard], self.y + DY[self.guard]
        
        if not self.is_inbound(new_x, new_y):
            return 0, 0, False
        else:
            if self.get_world_element(new_x, new_y) == '#' or (new_x, new_y) == self.extra_obstacle:
                self.turn()
                new_x, new_y = self.x + DX[self.guard], self.y + DY[self.guard]

        return new_x, new_y, True


    def move(self):
        new_x, new_y = self.x + DX[self.guard], self.y + DY[self.guard]
        self.out_of_bound = not self.is_inbound(new_x, new_y)

        if not self.out_of_bound:
            if self.get_world_element(new_x, new_y) == '#' or (new_x, new_y) == self.extra_obstacle:
                self.turn()
                new_x, new_y = self.x + DX[self.guard], self.y + DY[self.guard]

            self.x, self.y = new_x, new_y
            
            self.in_cycle = (self.x, self.y, self.guard) in self.path
            self.path.add((self.x, self.y, self.guard))


if __name__ == '__main__':
    world = World()
    cycles = 0

    while not world.out_of_bound:
        state = world.give_state()

        next_x, next_y, in_bound = world.next_pos()
        if in_bound:
            world.extra_obstacle = (next_x, next_y)
            while not world.in_cycle and not world.out_of_bound:
                world.move()
            cycles += world.in_cycle
            world.extra_obstacle = None

        world.set_state(state)
        world.move()

    print(cycles)
