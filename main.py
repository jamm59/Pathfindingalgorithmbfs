#using breath first search to find the path on an algorithm
from time import sleep
board = [
	[1,1,0,1,1,1,1,1,1,1],
	[1,1,0,1,1,0,0,0,0,5],
	[1,1,0,1,1,0,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,0,1,1,1,1,1],
	[1,1,1,1,0,1,1,1,1,1]
]


def print_board(brd):
	for row in range(0,len(brd)):
		print(""" 
		""")
		for col in range(0,len(brd[0])):
			if col == 0:
				print(end='')
			else:
				print('|',end='')

			if brd[row][col] == 1:
				print(f'  # ',end='')
			elif brd[row][col] == 0:
				print(' __ ',end='')
			else:
				print(f'{brd[row][col]}',end='')


def border(pos,bd):	
	row = pos[0]
	col = pos[1]

	if row >= len(bd)-1 or \
		row < 0 or \
		col > len(bd[0])-1 or \
		col < 0 :
		return True
	return False

def wall(pos,bd):		
	row = pos[0]
	col = pos[1]

	if bd[row][col] == 1:
		return True
	return False

def valid_path(pos,bd):
	if border(pos,bd) or wall(pos,bd):
		return False
	return True

def performbfs(pos,bd):
	queue = [pos]
	while queue != []:
		row = pos[0]
		col = pos[1]

		direction = [
			(-1,0),#top
			(0,-1), #left
			(1,0),#down
			(0,1),#right	
			]
		
		for dir in direction:
			new_x = row + dir[0]
			new_y = col + dir[1]

			if not valid_path((new_x,new_y),bd):
				print((new_x,new_y))
				continue

			elif valid_path((new_x,new_y),bd):
				queue.append((new_x,new_y))

		valid = queue.pop(0)
		if bd[valid[0]][valid[1]] == 5:
			break
		bd[valid[0]][valid[1]] = ' ?? '
		# sleep(1)
		print_board(bd)
		pos = valid
	print('Path found')

def main():
	print_board(board)
	print('\n\n\t\t Enter both the row and col index position of the board\n(for example row at position 3 and column at position 0)\n\n')
	while True:
		row,col = input('row: '),input('col: ')

		if not row.isdigit() or not col.isdigit():
			print('Please enter intergers only')
			continue
		else: 
			if len(str(row)) == 1 and len(str(col)) == 1 and border((int(row),int(col)),board) and board[int(row)][int(col)] == 0:
				row,col = int(row),int(col)
				break
			else:
				print('You have entered more than one int or choose a valid position')
				continue

	performbfs((row,col),board)


main()