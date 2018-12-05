import unittest


def find_path(grid, row, col, path, visited):
    if row < 0 or col < 0 or not grid[row][col] or (row, col) in visited:
        return False
    at_origin = row == 0 and col == 0

    if (at_origin or find_path(grid, row, col-1, path, visited) or find_path(grid, row-1, col, path, visited)):
        path.append((row, col))
        return True

    visited.add((row, col))

    return False
    
        
def robot_in_a_grid(grid):
    if not grid or len(grid) == 0:
        return None
    
    path = []
    visited = set()
    return path if find_path(grid, len(grid)-1, len(grid[0])-1, path, visited) else None


class Test(unittest.TestCase):
    def test_find_path(self):
        self.assertIsNone(robot_in_a_grid(None))
        self.assertIsNone(robot_in_a_grid([[]]))
        self.assertIsNone(robot_in_a_grid([[None, None], [None, None]]))

        grid = [[1, 1, 1], [None, 1, 1], [None, None, 1]]
        expected = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]

        self.assertEqual(expected, robot_in_a_grid(grid))


if __name__ == '__main__':
    unittest.main()