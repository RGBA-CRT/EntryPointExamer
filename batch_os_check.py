import os
import subprocess as sp
import sys

args = sys.argv
# print(args)
# tet = input()
if len(args) <2:
	exit(-1)
# print(args[1].encode('utf-8'))
exepath=args[1]

epxdir = os.path.dirname(__file__)
print(epxdir)

filenames = [f.name for f in os.scandir(epxdir) if f.name.endswith('.info')]

epxpath = os.path.join(epxdir, "epx.exe")
print(epxpath)

results={}
for file in filenames:
	print(file)
	infopath = os.path.join(epxdir, file)
	cmdline="{} --os-info {} {}".format(epxpath, infopath, exepath)
	print(cmdline)
	try:
		ls_file_name = sp.check_output(cmdline, shell=True).decode('utf-8').strip().split('\n')
		results[file] = True
	except sp.CalledProcessError as e:
		results[file] = False
print("====================================")
for retkey in results.keys():
	print("{:<20}\t{}".format(retkey,str(results[retkey])))

print("press enter")
tet = input()