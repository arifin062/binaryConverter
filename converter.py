import os; import sys; import time
menu_converter = '''
    ____________________________________
   |                                    |
   | [01] Convert bilangan Biner        |
   | [02] Convert bilangan Octal        |
   | [03] Convert bilangan Desimal      |
   | [04] Convert bilangan Hexadesimal  |
   |                                    |
   | [00] Exit                          |
   |____________________________________|'''

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
def user(st = ''):
	return raw_input('\t ' + st)
class convert():
	BIN = '\n\t Nilai bilangan Biner : '
	OCT = '\n\t Nilai bilangan Octal : '
	DES = '\n\t Nilai bilangan Desimal : '
	HEX = '\n\t Nilai bilangan Hexadesimal : '
	Invalid = '\n\t </Error> Bilangan salah\n'
	def __init__(self, bilangan):
		self.bilangan = bilangan
	def biner(self, bil):
		try:
			B = self.BIN + bil
			D = self.DES + str(int(bil, 2))
			O = self.OCT + str(oct(int(bil, 2)))
			H = self.HEX + str(hex(int(bil, 2))).replace('0x', '')
			return B + O + D + H + '\n'
		except ValueError:
			return self.Invalid
	def octal(self, bil):
		try:
			O = self.OCT + bil
			D = self.DES + str(int(bil, 8))
			B = self.BIN + str(bin(int(bil, 8))).replace('0b', '')
			H = self.HEX + str(hex(int(bil, 8))).replace('0x', '')
			return B + O + D + H + '\n'
		except ValueError:
			return self.Invalid
	def desimal(self, bil):
		try:
			D = self.DES + bil
			O = self.OCT + str(oct(int(bil, 10)))
			B = self.BIN + str(bin(int(bil, 10))).replace('0b', '')
			H = self.HEX + str(hex(int(bil, 10))).replace('0x', '')
			return B + O + D + H + '\n'
		except ValueError:
			return self.Invalid
	def hexades(self, bil):
		try:
			H = self.HEX + bil
			D = self.DES + str(int(bil, 16))
			O = self.OCT + str(oct(int(bil, 16)))
			B = self.BIN + str(bin(int(bil, 16))).replace('0b', '')
			return B + O + D + H + '\n'
		except ValueError:
			return self.Invalid
def main():
	os.system('clear')
	os.system('figlet Converter')
	print 'Author : ardyengineer@gmail.com'
	print 'Robotika Community - Banyuwangi 68482'
	print menu_converter + '\n'
	try:
		usr = int(user('[+]> : '))
	except ValueError:
		usr = 100
	print ''
	conv = convert('conv')
	if usr == 1:
		Bin = user(conv.BIN); print conv.biner(Bin)
	elif usr == 2:
		Oct = user(conv.OCT); print conv.octal(Oct)
	elif usr == 3:
		Des = user(conv.DES); print conv.desimal(Des)
	elif usr == 4:
		Hex = user(conv.HEX); print conv.hexades(Hex)
	elif usr == 0:
		sys.exit()
	else:
		time.sleep(2)
		restart_program()
if __name__=='__main__':
	main()