import unittest 


def fill_screen(screen, row, col, orig_color, new_color):
    if row < 0 or row >= len(screen)  or col < 0 or col >= len(screen[0]):
        return 

    if screen[row][col] == orig_color:
        screen[row][col] = new_color
        fill_screen(screen, row-1, col, orig_color, new_color)
        fill_screen(screen, row+1, col, orig_color, new_color)
        fill_screen(screen, row, col-1, orig_color, new_color)
        fill_screen(screen, row, col+1, orig_color, new_color)


def paint_fill(screen, row, col, color):
    if screen[row][col] != color:
        fill_screen(screen, row, col, screen[row][col], color)


class Test(unittest.TestCase):
    def test_paint_fill(self):
        screen = [[255, 255, 255], [255, 0, 255], [255, 0, 0]]
        paint_fill(screen, 1, 1, 127)

        expected = [[255, 255, 255], [255, 127, 255], [255, 127, 127]]
        self.assertEqual(expected, screen)


if __name__ == '__main__':
    unittest.main()
    