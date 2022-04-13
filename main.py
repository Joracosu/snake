from entities import Board, Snake, Depth


def modulo_10_p_7(n,p):
    ''' 
    Initially, a function was made to determine the Modulo 10^9+7, but the processing speed is slow and 
    that value is never going to be reachable with this algorithm. For this reason a Modulo 10^p+7 has 
    been used instead.
    '''
    M = 10**p+7
    return n % M


def numberOfAvailableDifferentPaths(board, snake, depth, solution=[], step=0, j=0):
    '''
    This algorithm follows the 'Branch and Pount' philosopy. It iterates in deep for each solution in a 
    method called 'Depth First Search' (DFS). Basically it follow the next scheme:
    
        1. Form a sequence of elements as a queue with the root element of the tree.
        2. Test if the first element in the queue is a final solution. In case of yes, we're done. 
           Otherwise, we continue with step 3.
        3. Remove the node explored in step 2 and add to the beginning of the queue all its child nodes.
        4. If there are no knots in the tail, then we cannot find the solution. Otherwise, we repeat step 2.
    '''
    # The exploration of possible movements is performed in the same order as defined here
    MOVES = ['L', 'U', 'R', 'D']

    # Load of classes in order to check the integrity of all parameters. If any constrain fails, the full code fails.
    # Also some methods are declared into 'Snake' class
    defined_board = Board(board)
    defined_snake = Snake(board, snake)
    defined_depth = Depth(depth)
    
    # array to store the current solutions
    solution = ([''] * depth) if not solution else solution
    
    # a copy of current snake position  is necessary to go back to previous step and continue exploring the tree
    n_snake = snake
    
    # For each possible movement...
    for i in MOVES:
        # the last viable state of the snake is loaded.
        snake = n_snake
        # The move is stored in the 'solution' array
        solution[step] = i
        # If the movement is allowed (no body-clash and inside board)...
        if defined_snake.viable_solution(snake, i):
            # calculate the new position of the snake.
            snake = defined_snake.move_snake(snake, i)
            # If the depth is reached...
            if step == depth - 1:
                # sum 1 to the total and print the solution
                j = j + 1
                print('Solution '+str(j)+':', ''.join(solution))
            # Otherwise...
            else:
                # keep exploring deeper the possible solution
                j = numberOfAvailableDifferentPaths(board, snake, depth, solution, step + 1, j)
        # In anyway, the last step is removed, preparing the 'solution' array for the next possible move and loop
        solution[step] = ''
        
        # If the total amount of solutions reach the limit defined by module 10^p+7, the algorithm stops
        # the value p=9 is settled as the paper ask for it, but it is unreachable
        if j > modulo_10_p_7(j, 9): return j
    return j
    

'''
Following there are the three tests proposed in the Challenge paper
'''
print('TEST 1')
board = [4, 3]
snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3
solutions = numberOfAvailableDifferentPaths(board, snake, depth)
print('Total solutions: ' + str(solutions))
print('\n')

print('TEST 2')
board = [2, 3]
snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
depth = 10
solutions = numberOfAvailableDifferentPaths(board, snake, depth)
print('Total solutions: ' + str(solutions))
print('\n')

print('TEST 3')
board = [10, 10]
snake = [[5, 5], [5, 4], [4, 4], [4,5 ]]
depth = 4
solutions = numberOfAvailableDifferentPaths(board, snake, depth)
print('Total solutions: ' + str(solutions))
