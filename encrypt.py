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
	else:
		None
			
	
	key=getRandom()
		
	iv=getRandom()
		
	keyFile="ENCRYPTION_DATA_"+mode+"_"+ args.input
	
		
		
	keyFile=keyFile[:keyFile.find(".")] #removing extension
	with open(keyFile,"w") as file:
		file.write(key)
		file.write("\n"+iv)
		
	
	comand=	"openssl enc  -aes-128-"+mode+" -e -in "+args.input+" -out "+args.output+" -k "+key+" -iv "+iv
	print(comand)
	os.system(comand)


def main():
	parser=argparse.ArgumentParser(description="Encrypt a file")
	parser.add_argument("-in",help="input file" ,dest="input", type=str, required=True)
	parser.add_argument("-out",help="output filename" ,dest="output", type=str, required=True)
	parser.add_argument("-enc",help="Encryption type (ecb,cbc,cfb,ofb)" ,dest="encryption", type=str, required=True)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)



def getRandom():
	out=""
	with open("/dev/urandom","rb") as file:
		buf= file.read(16)
		for i in buf:
			hexStr= (str(hex(ord(i))))[2:] # geting only 2 last digts of "0xff"
			out=out+hexStr # making string out of hex digits
		return out
	
def checkAccess(filename,access):
	#checks if file eists and one of access types
	if (os.path.exists(filename) and os.access(filename,access)  ):
		return True
	else:
		return False
		
		


if __name__=="__main__":
	main()

