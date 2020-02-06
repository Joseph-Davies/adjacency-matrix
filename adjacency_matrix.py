#/usr/bin/python
#Joseph Davies

class nxn_matrix:
	def __init__(self, width, height, initial_data = None):
		self._width = width
		self._height = height
		self._data = initial_data
		if initial_data == None:
			self._initial_matrix()
		
	def _initial_matrix(self):
		self._data = [None] * self._width * self._height
		
	def _i2dr(self, x, y):
		return self._data[((y % self._height) * self._width) + (x % self._width)]
	def _set_i2dr(self, x, y, val):
		self._data[((y % self._height) * self._width) + (x % self._width)] = val
		
	def __repr__(self):
		return "nxn_matrix({0}, {1}, {2})".format(self._width, self._height, self._data)

	def __str__(self):
		output = ""
		max_size = 0
		for x in range(self._width):
			for y in range(self._height):
				length = len(str(self._i2dr(x, y)))
				if length > max_size:
					max_size = length
		
		for y in range(self._height):
			output += "| "
			for x in range(self._width):
				output += ("{0:" + str(max_size) + "}").format(self._i2dr(x, y)) + " "
			output += "|\n"
		
		return output
	
	#----------------------------arithmetic operations-------------------------------------------
	def __add__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] += other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] += other
				i += 1
			return output
		
	def __radd__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] += other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] += other
				i += 1
			return output
	
	def __sub__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] -= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] -= other
				i += 1
			return output
	
	def __rsub__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] -= self._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] -= self
				i += 1
			return output
	
	def __mul__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other
				i += 1
			return output
	
	def __rmul__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other
				i += 1
			return output
	
	def __truediv__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] /= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] /= other
				i += 1
			return output
	
	def __floordiv__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] //= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] //= other
				i += 1
			return output
	
	def __rtruediv__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] /= self._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] /= self
				i += 1
			return output
	
	def __rfloordiv__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] //= self._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] //= self
				i += 1
			return output
	
	def __mod__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] *= other
				i += 1
			return output
	
	def __rmod__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] %= self._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(other._width, other._height, other._data.copy())
			i = 0
			while i < len(other._data):
				output._data[i] %= self
				i += 1
			return output
		
	def __pow__(self, other):
		if type(other) is nxn_matrix:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] **= other._data[i]
				i += 1
			return output
		else:
			output = nxn_matrix(self._width, self._height, self._data.copy())
			i = 0
			while i < len(self._data):
				output._data[i] **= other
				i += 1
			return output
			
	#--------------------------------------assignment operations-----------------------------	
	def __iadd__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] += other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] += other
				i += 1
	
	def __isub__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] -= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] -= other
				i += 1
	
	def __imul__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] *= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] *= other
				i += 1
	
	def __itruediv__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] /= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] /= other
				i += 1
	
	def __ifloordiv__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] //= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] //= other
				i += 1
	
	def __imod__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] %= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] %= other
				i += 1
	
	def __ipow__(self, other):
		if type(other) is nxn_matrix:
			i = 0
			while i < len(self._data):
				self._data[i] **= other._data[i]
				i += 1
		else:
			i = 0
			while i < len(self._data):
				output._data[i] **= other
				i += 1
				
	#----------------------------------other operations------------------------------------
	def __neg__(self):
		output = nxn_matrix(self._width, self._height, self._data.copy())
		i = 0
		while i < len(self._data):
			output._data[i] = -output.data[i]
			i += 1
		return output
	
	def __pos__(self):
		output = nxn_matrix(self._width, self._height, self._data.copy())
		i = 0
		while i < len(self._data):
			output._data[i] = +output.data[i]
			i += 1
		return output
		
	def __abs__(self):
		output = nxn_matrix(self._width, self._height, self._data.copy())
		i = 0
		while i < len(self._data):
			output._data[i] = abs(output.data[i])
			i += 1
		return output
		
	def __floor__(self):
		output = nxn_matrix(self._width, self._height, self._data.copy())
		i = 0
		while i < len(self._data):
			output._data[i] = math.floor(output.data[i])
			i += 1
		return output
	
	def __floor__(self):
		output = nxn_matrix(self._width, self._height, self._data.copy())
		i = 0
		while i < len(self._data):
			output._data[i] = math.ciel(output.data[i])
			i += 1
		return output
		
	#------------------------------------matrix operations-------------------------------------
	def dot(self, other):
		if self._width != other._height:
			print("Error: cannot multiple matrixies of size {0}x{1} and {2}x{3}".format(self._width, self._height, other._width, other._height))
		output = nxn_matrix(self._height, other._width)
		
		for first_y in range(self._height):
			for second_x in range(other._width):
				cell_sum = 0
				for x in range(self._width):
					self._i2dr(x, first_y)
					other._i2dr(second_x, x)
					small_sum = self._i2dr(x, first_y) * other._i2dr(second_x, x)
					cell_sum += small_sum
				output._set_i2dr(second_x, first_y, cell_sum)
		return output
	
	def matrix_multiply(self, other):
		self.dot(other)
	
	def _sub_matrix(self, matrix, pos):
		output = nxn_matrix(matrix._width - 1, matrix._height - 1)
		
		for width in range(output._width):
			for height in range(output._height):
				new_width = 0
				if width < pos: new_width = width
				else: new_width = width + 1
				output._set_i2dr(width, height, matrix._i2dr(new_width, height + 1))
		return output
			
	
	def determinant(self, matrix = None):
		if self._width != self._height:
			print('Error: cannot compute the determinant of a non square matrix')
		if matrix == None: matrix = self
		if matrix._width == 2:
			return (matrix._i2dr(0, 0) * matrix._i2dr(1, 1)) - (matrix._i2dr(0, 1) * matrix._i2dr(1, 0))
		output = 0
		sign = 1
		for thing in range(self._width):
			output += self._i2dr(thing, 0) * sign * self.determinant(self._sub_matrix(matrix, thing))
			sign *= -1
		
		return output
	
	def inverse(self, matrix = None):
		if matrix == None:
			matrix = self
		det = other.determinant()
		if deg == 0:
			print("Error: the other matrix has no determinant")
		output = nxn_matrix(matrix._width, matrix._height, matrix._data)
		coefficiant = 1 / deg
		return coefficiant * output
	
	def divide(self, other):
		output = nxn_matrix(self._width, self._height, self._data)
		
		return output * self.inverse(other)
		
		
		
		
	#---------------------------------------other functions-----------------------------------
	def get_raw_data_as_flat_list(self):
		return self._data
	
	def get_raw_data_as_2d_list(self):
		output = [None] * self._width
		for i in range(self._width):
			output[i] = [None] * self._height
		
		for x in range(self._width):
			for y in range(self._height):
				output[x][y] = self._i2dr(x, y)
		
		return output
	
	def get_width():
		return self._width
	
	def get_height():
		return self._height
	

class adjacency_matrix(nxn_matrix):
	def __init__(self, width, height):
		nxn_matrix.__init__(self, width, height)
		self._header = []
		
	def load_from_xml(self, xml_reader_instance):
		pass
		
	def load_from_matrix(self, matrix):
		self._data = matrix._data
		self._width = matrix._width
		self._height = matrix._height
	
	def set_header(self, header):
		self._header = header	
	
	def set(x, y, val):
		self._set_i2dr(x, y, val)
	
	def get(x, y)
		self._i2dr(x, y)
		
	def __str__(self):
		max_length = 0
		for name in self._header:
			if len(name) > max_length:
				max_length = len(name)
		for number in self._data:
			if len(str(number)) > max_length:
				max_length = len(str(number))
		
		output = ""
		output += " " * max_length
		output += "   "
		
		for name in self._header:
			output += ("{0:" + str(max_length) + "}").format(name)
			output += " "
		output += "  \n"
		
		
		for y in range(self._height):
			output += ("{0:" + str(max_length) + "}").format(header[y])
			if y == 0:
				output  += " " + u'\u250c' + " "
			elif y == self._height - 1:
				output  += " " + u'\u2514' + " "
			else:
				output += " " + u'\u2502' + " "
			for x in range(self._width):
				if x == y:
					output += " " * (max_length - 1)
					output += "x"
					output += " "
				else:
					output += ("{0:" + str(max_length) + "}").format(self._i2dr(x, y))
					output += " "
			if y == 0:
				output  += " " + u'\u2510' + " "
			elif y == self._height - 1:
				output  += " " + u'\u2518' + " "
			else:
				output += " " + u'\u2502' + " "
			
			output += "\n"
	
		return output




