import random
import heapq

def manhattan_distance(puzzle, goal):
    distance = 0
    goal_positions = {value: (i, j) for i, row in enumerate(goal) for j, value in enumerate(row)}
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

def a_star_search(start, goal):
    visited = set()
    frontier = []
    heapq.heappush(frontier, start)
    while frontier:
        current = heapq.heappop(frontier)
        if current.puzzle == goal.puzzle:
            return current
        visited.add(str(current.puzzle))
        for next_node in current.find_next_nodes():
            if str(next_node.puzzle) not in visited:
                heapq.heappush(frontier, next_node)
    return None

def generate_puzzle():
    puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    numbers = list(range(1, 9))
    for i in range(3):
        for j in range(3):
            if i == 2 and j == 2:
                break
            index = random.randint(0, len(numbers) - 1)
            puzzle[i][j] = numbers[index]
            numbers.pop(index)
    return puzzle


class Node:
    def __init__(self, puzzle, movement, depth, manhattan, previous):
        self.depth = depth
        self.puzzle = puzzle
        self.movement = movement
        self.manhattan = manhattan
        self.previous = previous

    def __lt__(self, other):
        return (self.depth + self.manhattan) < (other.depth + other.manhattan)


    def move_piece(self, movement):
        puzzle = self.puzzle
        new_puzzle = [row.copy() for row in puzzle]
        x, y = next((i, j) for i in range(3) for j in range(3) if puzzle[i][j] == 0)

        if movement == 'up':
            if x > 0:
                new_puzzle[x][y], new_puzzle[x - 1][y] = new_puzzle[x - 1][y], new_puzzle[x][y]
                return new_puzzle
        elif movement == 'down':
            if x < 2:
                new_puzzle[x][y], new_puzzle[x + 1][y] = new_puzzle[x + 1][y], new_puzzle[x][y]
                return new_puzzle
        elif movement == 'left':
            if y > 0:
                new_puzzle[x][y], new_puzzle[x][y - 1] = new_puzzle[x][y - 1], new_puzzle[x][y]
                return new_puzzle
        elif movement == 'right':
            if y < 2:
                new_puzzle[x][y], new_puzzle[x][y + 1] = new_puzzle[x][y + 1], new_puzzle[x][y]
                return new_puzzle
        return None

    def find_next_nodes(self):
        next_nodes = []
        movements = ['up', 'down', 'left', 'right']
        for movement in movements:
            new_puzzle = self.move_piece(movement)
            if new_puzzle is not None:
                next_nodes.append(Node(new_puzzle, movement, self.depth + 1, manhattan_distance(new_puzzle, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]), self))
        return next_nodes

    def next_way(self, start):
        way = []
        current = self
        while current != start:
            way.append(current)
            current = current.previous
        way.append(start)
        way.reverse()
        return way

    def print(self):
        for row in self.puzzle:
            print(' '.join(f'{num:2}' for num in row))
        print('')


def main():
    puzzle = generate_puzzle()
    start = Node(puzzle, '', 0, 0, None)
    ##puzzle_manual = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
    ##start = Node(puzzle_manual, '', 0, 0, None)
    goal = Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]], '', 0, 0, None)

    print('Puzzle inicial:')
    start.print()
    print("========================================")

    result = a_star_search(start, goal)
    if result is not None:
        path = result.next_way(start)
        path.pop(0)
        for node in path:
            print(f'Movimiento: {node.movement}')
            node.print()

        print(f'Solucion encontrada en: {result.depth} movimientos')
    else:
        print('No se encontro solucion')


if __name__ == '__main__':
    main()
