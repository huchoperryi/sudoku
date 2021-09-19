import numpy as np
import sys

class SudokuCell():
	
	
	def __init__(self):
		
		self.judge = [True] * 9
		self.is_fixed = False
		self.value = ' '
		
		
	def SetValue(self, value):
		
		if (value < 1 or
				value > 9 or
				type(value) is not int):
					value = 0
		
		if self.is_fixed == True:
			#print("It's fixed cell")
			return 1
		elif value == 0:
			return 2
			
		else:
			self.is_fixed = True
			self.value = value
			for i in range(9):
				if i != value - 1:
					self.judge[i] = False
			return 0
			
	def FixCheck(self):
		
		count = 0
		tmp_value = 0
		if self.is_fixed:
			return
		for i in range(9):
			if self.judge[i] == True:
				count += 1
				tmp_value = i
		if count == 1:
			self.SetValue(tmp_value + 1)
			return 0


	def DelJudge(self, index):
		
		self.judge[index] = False
	
		if sum(self.judge) == 0:
			print('all candidate delited.')
		
class SudokuField():
	
	def __init__(self):
		print('set field')
		#self.rows = [[None] * 9] * 9
		self.rows =[]
		self.cols = []
		self.areas = []
		
		for i in range(9):
			row = []
			for j in range(9):
				row.append(SudokuCell())
			self.rows.append(row)
		
		for i in range(9):
			col = []
			area = []
			for j in range(9):
				#self.cols[i][j] = self.rows[j][i]
				col.append(self.rows[j][i])
				
				wk_i = i // 3 * 3 + j // 3
				wk_j = i % 3 * 3 + j % 3
				area.append(self.rows[wk_i][wk_j])
				
			self.cols.append(col)
			self.areas.append(area)
		"""
		for i in range(9):
			for j in range(9):
				self.rows[i][j].SetValue(i * 9 + j + 1)
		"""
	def CutOtherJudge(self, block, no, value):
		
		for i in range(9):
			
			block[i]
	
	def CutJudge(self, row, col):
		
		if self.rows[row][col].value != ' ':
			idx = self.rows[row][col].value - 1
			area = row // 3 * 3 + col // 3
			add = row % 3 * 3 + col % 3
		
		#if idx != ' ':
			for i in range(9):
				if i !=col:
					self.rows[row][i].DelJudge(idx)
				if i != row:
					self.cols[col][i].DelJudge(idx)
				if i != add:
					self.areas[area][i].DelJudge(idx)
	
	
	def CutJudgeAll(self):
		
		for i in range(9):
			for j in range(9):
				self.CutJudge(i, j)
		
		
	def CheckAll(self):
		count = 0
		for i in range(9):
			for j in range(9):
				result = self.rows[i][j].FixCheck()
				if result == 0:
					count += 1
		#print('{} cell fixed'.format(count))
		return count
		
		
	def ScanBlock(self, block):
		
		for value in range(9):
			count= 0
			tmp_add = 0
			for add in range(9):
				if block[add].judge[value] == True:
					count += 1
					tmp_add = add
			if (count == 1 and
					block[tmp_add].is_fixed == False):
				"""
				print('add:{} value:{}'.format(tmp_add,value))
				for i in range(9):
					print('block {}:'.format(i), end='')
					for j in range(9):
						if block[i].judge[j]:
							print('t',end='')
						else:
							print('.',end='')
					print('')
				"""
				block[tmp_add].SetValue(value + 1)
		
		
	def Solve(self):
		check = 1
		
		#while check > 0:
		for i in range(10):
			self.CutJudgeAll()
			for i in range(9):
				self.ScanBlock(self.rows[i])
				self.ScanBlock(self.cols[i])
				self.ScanBlock(self.areas[i])
				
			check = self.CheckAll()
			#print('{} cell fixed'.format(check))
			#self.ShowWithCandidate()
		
		
	def SetTask(self, 
		task =	[[0,0,0, 0,0,0, 9,0,0],
						 [0,0,0, 4,9,0, 0,0,6],
						 [0,9,6, 0,0,0, 0,4,0],
						 [0,0,0, 0,8,0, 7,0,0],
						 [0,2,0, 0,3,7, 5,1,0],
						 [5,0,0, 0,2,0, 3,8,0],
						 [9,6,0, 1,0,0, 4,0,0],
						 [8,5,4, 0,7,0, 0,2,1],
						 [0,3,0, 0,0,0, 8,0,0]]
				):
		for i in range(9):
			for j in range(9):
				self.rows[i][j].SetValue(task[i][j])
				
		
	def show(self):
		
		for row in range(9):
			for col in range(9):
				value = self.rows[row][col].value
				print('{}'.format(value), end='')
				if col % 3 == 2 and col != 8:
					print('|', end='')
			print('')
			if row % 3 == 2 and row != 8:
				print('---+---+---')
				
	def ShowWithCandidate(self):
		print('Show with candidate')
		for i in range(9):
			for j in range(9):
				if self.rows[i][j].is_fixed:
					fix = 'F'
				else:
					fix = ' '
				print('*{}{}|'.format(self.rows[i][j].value, fix), end='')
			print('')
			for jr in range(0,9,3):
				for j in range(9):
					str_judge = ''
					for k in range(3):
						if self.rows[i][j].judge[jr+k]:
							str_judge = str_judge + str(jr+k+1)
						else:
							str_judge = str_judge + '.'
					print('{}|'.format(str_judge), end='')
				print('')
			if i % 3 == 2:
				print('')

if __name__ == '__main__':
	
	field = SudokuField()
	print('set task')
	field.SetTask()
	field.show()
	#field.ShowWithCandidate()
	print('solve')
	field.Solve()
	field.show()
	#field.ShowWithCandidate()
