#!/usr/bin/env python

#version for python 2.7 which is used on vm
import sys, os, argparse

 
def run(args):

	encryption= args.encryption
	if (encryption=="ecb"):
		mode="ecb"
	elif (encryption=="cbc"):
		mode="cbc"
	elif (encryption=="cfb"):
		mode="cfb"
	elif (encryption=="ofb"):
		mode="ofb"
	else:
		print ("invalid encryption ")
		sys.exit()
	
	#checks input file
	if not(checkAccess(args.input, os.R_OK)):
		print ("Can not acces input ")
		sys.exit()
	#checks output file
	if(os.path.exists(args.output)):
		if not(checkAccess(args.output, os.W_OK)):
			print ("Can not acces input ")
			sys.exit()
	
	#checks credFile
	if(os.path.exists(args.credFile)):
		if not(checkAccess(args.credFile, os.R_OK)):
			print ("Can not acces credFile ")
			sys.exit()
	else:
		None
			
	

	
		

	with open(args.credFile,"r") as file:
		lines= file.read().splitlines()
		key=lines[0]
		iv=lines[1]
		
	
	comand=	"openssl enc -d -aes-128-"+mode+" -in "+args.input+" -out "+args.output+" -k "+key+" -iv "+iv
	print(comand)
	os.system(comand)


def main():
	parser=argparse.ArgumentParser(description="Encrypt a file")
	parser.add_argument("-in",help="input file" ,dest="input", type=str, required=True)
	parser.add_argument("-out",help="output filename" ,dest="output", type=str, required=True)
	parser.add_argument("-enc",help="Encryption type (ecb,cbc,cfb,ofb)" ,dest="encryption", type=str, required=True)
	parser.add_argument("-credFile",help="File with key in first line and initialization vector in second." ,dest="credFile", type=str, required=True)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)




	
def checkAccess(filename,access):
	#checks if file eists and one of access types
	if (os.path.exists(filename) and os.access(filename,access)  ):
		return True
	else:
		return False
		
		


if __name__=="__main__":
	main()

