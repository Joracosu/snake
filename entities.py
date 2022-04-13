'''
This pack of classes has been developed in order to check the integrity of the values in a compacted way.
Some properties are useless, but in future develops they can be used for something.

The boundary check handle has been developed in order to raise code errors. With another approach, input 
management could be included.
'''


'''
In 'Board' class, is not necessary to set a property for rows, columns or size, nevertheless 
they are being used to check the boundaries.
'''
class Board:
    def __init__(self, dimensions):
        self.size = len(dimensions)
        self.rows = dimensions[0]
        self.columns = dimensions[1]
        self.workboard = dimensions

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value != 2: 
            raise ValueError('Incorrect board size.')
        self._size = 2

    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, value):
        if value < 0 or value > 10:
            raise ValueError('Incorrect board rows.')
        self._rows = value

    @property
    def columns(self):
        return self._columns
    
    @columns.setter
    def columns(self, value):
        if value < 0 or value > 10:
            raise ValueError('Incorrect board columns.')
        self._columns = value


'''
As happens with previous class, in this case the 'Depth' class only pretends to check the constrains 
defined in the Challenge paper
'''
class Depth:
    def __init__(self, value):
        self.size = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value < 1 or value > 20:
            raise ValueError('Path depth is out of length.')
        self._size = value        

        
'''
A 'Snake_Segment' class has been created only to manage the integrity of the snake. This class is later 
called from the 'Snake' class at the beginning of the algorithm
'''        
class Snake_Segment:
    def __get__(self, obj, value):
        return self.value

    def __set__(self, obj, value):
        # For each segment...
        for i in value:
            # if the dimension is different from 2
            if len(i) != 2:
                raise ValueError('Segment dimension incoherent.')
        # For each segment except the head...
        for n in range(1,len(value)):
            # auxiliary variables to make the check code more readable: 
            #    d0 -> dimension row        d1 -> dimension column
            #    n0 -> previous segment     n1 -> current segment
            d0n0 = value[n-1][0]
            d0n1 = value[n][0]
            d1n0 = value[n-1][1]
            d1n1 = value[n][1]
            # Two double checks are made at the same time. If none of them are reached, then fails:
            #    If row dimension remains equal and the column dimension differs one unit
            #  or
            #    If column dimension remains equal and the row dimension differs one unit
            if not(d0n0 == d0n1 and abs(d1n0-d1n1) == 1 or d1n0 == d1n1 and abs(d0n0-d0n1) == 1):
                raise ValueError('There is some discontinuity in the snake definition.')        
        self.value = value    

        
'''
Unlike the previous classes, this class is not only used to check the established constrains and the 
integrity of the data. It also contains a pack of methods to be used to calculate the position of the 
snake in its movement and to verify the feasibility of those movements.
'''
class Snake:
    body = Snake_Segment()
    def __init__(self, board, segments):
        self.length = len(segments)
        self.body = segments
        self.board = board
        if self.body_clash(segments):
            raise ValueError('Snake is clasing with itself.')
        if self.body_outside_boundaries(segments):
            raise ValueError('Snake body out of board.')

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value < 3 or value > 7:
            raise ValueError('Incorrect snake length.')
        self._length = value
    
    # Determine if in the current position of the snake, there is any clash of segments
    def body_clash(self, value):
        # Empty dictionary where each segment studied will be stored
        set_snake = set()
        for segment in value:
            # if a segment is found in the dictionary, there is a clash and the check is finished
            if tuple(segment) in set_snake:
                return True
            # otherwise the segment is added to the dictionary
            else:
                set_snake.add(tuple(segment))         
        return False
    
    # Determine if the full snake body is contained inside the play-board. Easily readable code
    def body_outside_boundaries(self, value):
        for n in range(len(value)):
            for m in range(2):
                if value[n][m] < 0 or value[n][m] >= self.board[m]:
                    return True
        return False
    
    # Translate the direction letter into the head move array
    def conver_direction(self, command):
        if command == 'L':
            move = [0,-1]
        if command == 'U':
            move = [-1,0]
        if command == 'R':
            move = [0, 1]
        if command == 'D':
            move = [1, 0]
        return move

    # Calculates the new position of the snake
    def move_snake(self, value, direction):
        # First calculate the new position of the head summing the direction array
        new_head = [[x + y for x, y in zip(value[0], self.conver_direction(direction))]]
        # The rest of the body is inherited from previous step
        new_body = value[0:len(value)-1]
        # The new snake is a concatenation
        new_snake = new_head + new_body
        return new_snake
    
    # Study if the current position of the snake is possible. This is the main method to determine 
    # the feasibility of the algorithm. A 'False' output of this function will pound the current branch.
    def viable_solution(self, value, direction):
        n_snake = self.move_snake(value, direction)
        if self.body_outside_boundaries(n_snake):
            return False
        if self.body_clash(n_snake):
            return False
        return True
    