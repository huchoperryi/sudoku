import numpy as np
import sys

class SudokuField():
	
	def __init__(self, initial):
		
		self.work_field = np.zeros((9,9,10),dtype=int)
		
		for i in range(9):
			for j in range(9):
				
				#[i][j][0] 要素に初期値を代入
				self.work_field[i][j][0] = initial[i][j]
				
				if initial[i][j] == 0:
					for k in range(9):
						self.work_field[i][j][k+1] = k + 1
				else:
				#[i][j][1-9]
					self.work_field[i][j][initial[i][j]]=initial[i][j]
					
					
	def del_candidete(self):
		
		for i in range(9):
			for j in range(9):
				#各マスを走査
				
				
				if self.work_field[i][j][0] != 0:
					fix = self.work_field[i][j][0]

					for k in range(9):
						if k != i:
							self.work_field[k][j][fix] = 0
						if k != j:
							self.work_field[i][k][fix] = 0
					
					for k1 in range(3):
						for k2 in range(3):
							if i-i%3+k1 != i or j-j%3+k2 != j:
								self.work_field[i-i%3+k1][j-j%3+k2][fix] = 0
	
	def unique_check(self):
		for i in range(9):
			for j in range(9):
				
				for k in range(9):
					if self.work_field[i][j][k+1] != 0:
						value = self.work_field[i][j][k+1]
						count = 0
						for v in range(9):
							if self.work_field[i][v][k+1] == value:
								count = count + 1
						if count == 1:
							for l  in range(9):
								if l + 1 != value:
									self.work_field[i][j][l+1] = 0
									
						count = 0
						for v in range(9):
							if self.work_field[v][j][k+1] == value:
								count = count + 1
						if count == 1:
							for l  in range(9):
								if l + 1 != value:
									self.work_field[i][j][l+1] = 0
	
	def display(self):
		print('Display field')
		
		for i in range(9):
			for j in range(9):
				if self.work_field[i][j][0] == 0:
					print('-', end='')
				else:
					print(self.work_field[i][j][0], end='')
				if (j+1)%3 == 0:
					print(' ', end='')
				
			print()
			if i%3 == 2:
				print()
			
	def display_with_candidate(self):
		print('Display with candidate')
		for i in range(9):
			for j in range(9):
				if self.work_field[i][j][0] == 0:
					print('*-* ', end='')
				else:
					print('*' +\
								str(self.work_field[i][j][0]) +\
							 '* ', end='')
			
			print()
			
			for ii in range(3):
				for jj in range(9):
					for k in range(3):
						
						if self.work_field[i][jj][ii*3+k+1] !=0:
							print(self.work_field[i][jj][ii*3+k+1], end='')
						else:
							print('.', end='')
					print(' ', end='')
				print()
		
	def fix_value(self):
		
		fixed_value = 0
		
		for i in range(9):
			for j in range(9):
				
				#[i][j][0]要素が0なら
				if self.work_field[i][j][0] == 0:
					count = 0
					value = 0
					#候補が1つに絞られていれば確定	
					for k in range(9):
						if self.work_field[i][j][k+1] != 0:
							count = count + 1
							value = self.work_field[i][j][k+1]
					if count == 1:
						self.work_field[i][j][0] = value
						fixed_value = fixed_value + 1
					
		return fixed_value
			
			
def input_problem():
	
	problem = [[0] * 9 for i in range(9)]
	print('Set problem')
	
	input_line = [input() for i in range(9)]
	
	for i in range(9):
		digit = 0
		j = 0
		
		#入力桁数まで または 9桁まで
		while digit < len(input_line[i]) and j < 9:
			
			#0-9ならprobremに代入
			if '0' <= input_line[i][digit] <= '9':
				problem[i][j] = int(input_line[i][digit])
				j = j + 1
				digit = digit + 1
			#空白は無視
			elif input_line[i][digit] == ' ':
				digit = digit + 1
			
			#それ以外(文字等)は0にする
			else:
				problem[i][j] = 0
				j = j + 1
				digit = digit + 1
	print('Initial set is:')
	for i in range(9):
		for j in range(9):
			print(problem[i][j],end='')
		print()
	ans = input('Input OK? y/n: ')
	
	if ans == 'y' or ans == 'Y':
		print('solve ...')
	else:
		input('Input reinput row number:')

	return problem
	

if __name__ == '__main__':
	# Set Probrem
	initial = [[0,0,0, 0,0,0, 9,0,0],
						 [0,0,0, 4,9,0, 0,0,6],
						 [0,9,6, 0,0,0, 0,4,0],
						 [0,0,0, 0,8,0, 7,0,0],
						 [0,2,0, 0,3,7, 5,1,0],
						 [5,0,0, 0,2,0, 3,8,0],
						 [9,6,0, 1,0,0, 4,0,0],
						 [8,5,4, 0,7,0, 0,2,1],
						 [0,3,0, 0,0,0, 8,0,0]]
						
	initial = input_problem()
	
	field = SudokuField(initial)
	
	if field == 0:
		print('input error')
		sys.exit()
		
	field.display()
	
	#field.display_with_candidate()
	
	fixed = 1
	
	while fixed != 0:
		field.del_candidete()
	
		#field.display_with_candidate()
		field.unique_check()
		
		fixed = field.fix_value()
	
		print(fixed)
	
	field.display_with_candidate()
	
	field.display()
