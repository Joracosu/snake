


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

        
class Snake_Segment:
    def __get__(self, obj, value):
        return self.value

    def __set__(self, obj, value):
        for i in value:
            if len(i) != 2:
                raise ValueError('Segment dimension incoherent.')
        for n in range(1,len(value)):
            d0n0 = value[n-1][0]
            d0n1 = value[n][0]
            d1n0 = value[n-1][1]
            d1n1 = value[n][1]
            if not(d0n0 == d0n1 and abs(d1n0-d1n1) == 1 or d1n0 == d1n1 and abs(d0n0-d0n1) == 1):
                raise ValueError('There is some discontinuity in the snake definition.')        
        self.value = value    

        
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
        
    def body_clash(self, value):
        set_snake = set()
        for n in range(len(value)):
            if tuple(value[n]) in set_snake:
                return True
            else:
                set_snake.add(tuple(value[n]))         
        return False
        
    def body_outside_boundaries(self, value):
        for n in range(len(value)):
            for m in range(2):
                if value[n][m] < 0 or value[n][m] >= self.board[m]:
                    return True
        return False
    
    def move_snake(self, value, direction):
        new_head = [[x + y for x, y in zip(value[0], self.conver_direction(direction))]]
        new_body = value[0:len(value)-1]
        new_snake = new_head + new_body
        return new_snake
        
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

    def viable_solution(self, value, direction):
        n_snake = self.move_snake(value, direction)
        if self.body_outside_boundaries(n_snake):
            return False
        if self.body_clash(n_snake):
            return False
        return True
    
    
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
   
        
        
        
        
        
        
        
        
        
        
        
        

    