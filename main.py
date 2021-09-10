counter = 0

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




# for i in range(99999999999999999999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999):
# 	collatz_conjecture(99999999999999999999999999999999999999999999999999999999999)
# 	print(counter)
# 	# print(i)

collatz_conjecture(99999999999999999999999999999999999999999999999999999999999)
print(counter)