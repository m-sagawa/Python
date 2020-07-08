import leap

def test_leap():
	year1 = 2000
	value = leap.isleap(year1)
	assert value == True

	year2 = 1900
	value = leap.isleap(year2)
	assert value == False

	year3 = 2004
	value = leap.isleap(year3)
	assert value == True

	year4 = 2001
	value = leap.isleap(year4)
	assert value == False