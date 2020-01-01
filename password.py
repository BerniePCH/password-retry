x = 1
while True:
	password = input('請輸入您的密碼： ')
	if password == 'a123456':
		print('登入成功！')
		break
	elif x < 3:
		x = x + 1
		y = 4 - x
		y = str(y)
		print('您還剩下'+y+'次機會')
	else:
		print('您的帳號已被鎖定')
		break

