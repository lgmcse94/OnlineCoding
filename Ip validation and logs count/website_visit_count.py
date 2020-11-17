
def read_write(file):
	dic={}
	try:
		with open(file) as f:
			for line in f:
				site=line.split(' - - ')[0].strip()
				if(site in dic):
					dic[site]=dic[site]+1
				else:
					dic[site]=1
	except (Exception) as error:
		print(error)
	#print(dic)

	with open('records_'+file, 'w') as f:
		for k,v in dic.items():
			f.write(str(k)+" "+str(v)+"\n")

read_write('hosts_access_log_00.txt')