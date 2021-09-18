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
			print("It's fixed cell")
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
		for i in range(9):
			if self.judge[i] == True:
				count += 1
				tmp_value = i
		if count == 1:
			self.SetValue(tmp_value + 1)
			return 0

class SudokuField():
	
	def __init__(self):
		print('set field')
		#self.raws = [[None] * 9] * 9
		self.raws =[]
		for i in range(9):
			raw = []
			for j in range(9):
				raw.append(SudokuCell())
			
			self.raws.append(raw)
			
		self.cols = []
		self.areas = []
		
		for i in range(9):
			col = []
			area = []
			for j in range(9):
				#self.cols[i][j] = self.raws[j][i]
				col.append(self.raws[j][i])
				
				wk_i = i // 3 * 3 + j // 3
				wk_j = i % 3 * 3 + j % 3
				area.append(self.raws[wk_i][wk_j])
				
			self.cols.append(col)
			self.areas.append(area)
		"""
		for i in range(9):
			for j in range(9):
				self.raws[i][j].SetValue(i * 9 + j + 1)
		"""
		
	def CutJudge(self, raw, col):
		
		if self.raws[raw][col].value != ' ':
			idx = self.raws[raw][col].value - 1
			area = raw // 3 * 3 + col // 3
			add = raw % 3 * 3 + col % 3
		
		#if idx != ' ':
			for i in range(9):
				self.raws[raw][i].judge[idx] = False
				self.cols[col][i].judge[idx] = False
				self.areas[area][i].judge[idx] = False
	
	
	def CutJudgeAll(self):
		
		for i in range(9):
			for j in range(9):
				self.CutJudge(i, j)
		
		
	def CheckAll(self):
		count = 0
		for i in range(9):
			for j in range(9):
				result = self.raws[i][j].FixCheck()
				if result == 0:
					count += 1
		#print('{} cell fixed'.format(count))
		return count
		
	
	def Solve(self):
		check = 1
		
		while check > 0:
		#for i in range(10):
			self.CutJudgeAll()
			check = self.CheckAll()
			print('{} cell fixed'.format(check))
		
		
	def SetTask(self):
		task = [[4,0,7, 0,1,0, 2,0,9],
				[0,1,0, 6,0,7, 0,8,0],
				[3,0,0, 0,0,0, 0,0,0],
				[0,4,0, 0,0,0, 0,1,0],
				[7,0,0, 0,0,0, 0,0,3],
				[0,3,0, 0,0,0, 0,5,0],
				[0,0,0, 0,0,0, 0,0,7],
				[0,5,0, 8,0,2, 0,6,0],
				[1,0,6, 0,9,0, 8,0,2]]
						
		for i in range(9):
			for j in range(9):
				self.raws[i][j].SetValue(task[i][j])
				
		
	def show(self):
		
		for raw in range(9):
			for col in range(9):
				value = self.raws[raw][col].value
				print('{}'.format(value), end='')
				if col % 3 == 2 and col != 8:
					print('|', end='')
			print('')
			if raw % 3 == 2 and raw != 8:
				print('---+---+---')

if __name__ == '__main__':
	
	field = SudokuField()
	print('set task')
	field.SetTask()
	field.show()
	print('solve')
	field.Solve()
	field.show()
