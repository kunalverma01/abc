def sorter1(a):
	if len(a)<= 1:
		return True
	else:
		return (a[0] <= a[1]) and sorter(a[1:])

def sorter2(a):
	if len(a)<= 1:
		return True
	else:
		return (a[-2] <= a[-1]) and sorter(a[:-1])