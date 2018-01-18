def check(number):
	temp = number
	for b in range(1,5):
		number = number + temp%10
		temp = temp/10
	return number
count = 0
summer = 0
for a in range(1,5000):
	fcount = 0
	while fcount < a:
		if a == check(fcount):
			break

		else:
			fcount = fcount+1
	if fcount == a:
		summer = summer + a
print(summer)
