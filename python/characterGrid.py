grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#we want to get below output
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....


for y in range(6):
	x = 0
	while x < 9:
		print (grid[x][y], end = " ")
		x = x+1
	print ()
		


	
