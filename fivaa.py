def fivaa(count):
	for index in range(1,count+1):
		print "{}{}".format(str(count-index)*2,str(count-index+2)*(count-index+1))

fivaa(5)