def collatz_conjecture(num):
	global counter
	counter+=1
	stored_num = 0
	if num % 2 == 0:
		stored_num = num / 2
		print("even -- ", stored_num)
	else:
		stored_num = num * 3 + 1 
		print("Odd -- ",stored_num)
	if stored_num == 1:
		return
	collatz_conjecture(stored_num)


counter = 0
collatz_conjecture(99)
print(counter)
