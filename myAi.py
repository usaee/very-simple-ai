#!/usr/bin/env python
#import personality
import signal
import sys
sys.path.append('/home/pi/')
import random
import time
import subprocess
import em
import datetime
from threading import Thread
from threading import Timer
#        VARIABLES GO HERE
#               |
#               |
#               V

debug = False
timedAns = None
holding = False
tOut = False
#
#	FUNCTIONS START HERE
#		|
#		|
#		V
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def interrupted():
	return
signal.signal(signal.SIGALRM, interrupted)
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func6(): # ---------------------> For thinking
	pass
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func5(): # --------------------> This is for when a conversation has ended or user isnt responding
        tmo = 'Hey, you still there?'
        func4(tmo)
        vv = func2()
        if vv == None:
                tmo2 = 'Bye!\n'
                func4(tmo2)
                return True
        else:
                return False
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func4(text): # --------------------> For Ai Texting/Talking
	ai = '\n\nAi: '
        sys.stdout.write(ai)
        sys.stdout.flush()
        for i in text:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.02)
	print '\n'
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func3(unk):	# --------------------> For handling unknown inputs
	global debug
	st = "I don't know how to respond to that..."
	func4(st) # Say this
	while True:
		st2 = 'What is a good way for me to respond to "{}" ...? '.format(unk)
		func4(st2) # Say this
        	v = func2() # Get Input
		v += '\n'
		unk += '\n'
		if v == None:
			vv = func5()
			if vv == True:
				break
			else:
				continue
		elif v == 'bye\n' or v == 'Bye' or v == 'see ya' or v == 'bye \n' or v == 'Bye ':
			st = 'Ok, see ya =)'
			func4(st)
			sys.exit()

		elif 'ask another' in v:
			st = 'Ohh gotcha =)'
			func4(st)
			f=open('nxTopic','a')
			f.write(unk)
			f.close()
			break

		elif 'no need' in v:
			if 'to respond' in v:
				break
			elif len(v) <= 9:
				break
			else:
	                        f = open('respondAi','a')
	                        f.write(v)
	                        f.close()
	                        f2 = open('userInputAi','a')
	                        f2.write(unk)
	                        f.close()
	                        st3 = '\nGot it, thank you! =)\n'
	                        func4(st3) # Say this
	                        break
		else:
			f = open('respondAi','a')
		        f.write(v)
		        f.close()
		        f2 = open('userInputAi','a')
		        f2.write(unk)
			f.close()
		        st3 = '\nGot it, thank you! =)\n'
			func4(st3) # Say this
			break
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func2():	# --------------------> For getting user input
	global debug
	global timedAns
	global holding
	f = open('preDic','a')
	try:
	        signal.alarm(40)		# Set timeout alarm in case the user leaves the computer or loses session
		v = raw_input('> ')
		v.lower()
		vv = v + '\n'
		f.write(vv)
		signal.alarm(0)
		f.close()
		v = v.rstrip()
		return v
	except:
		f.close()
		return
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def soci():
	rep = False
	while True:
		if rep == False:
			st = 'Can you teach me something to say?'
			func4(st)		# Say this
		v = func2()
		if v == 'y' or v == 'yes' or v == 'sure' or v == 'sure!' or v == 'yea!' or v == 'yea':
			v2 = func2()
		        f = open('socialAi','r')
		        frl = f.readlines()
		        f.close()
			try:
				frl.index(v2)
				st = 'Thanks but I already learned how to say that. Could you teach me something else? '
				func4(st)		# Say this
				rep = True
			except:
				v2 += '\n'
				f = open('socialAi','a')
				f.write(v2)
				f.close()
				break
		elif v == 'bye' or v == 'Bye' or v == 'see ya':
			st = 'Ok, see ya =)'
			func4(st)
			sys.exit()
		else:
			st = 'Darn it =/'
			func4(st)		# Say this
			break
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def func1(): # --------------------> For Ai Logic
	global debug
	cnt = 0
#	ai = '\nAi: '
	list = []
	list2 = []
	lif = sum(1 for line in open('socialAi'))	# gets number of lines in this file
	f = open('socialAi','r')
	frl = f.readlines()
	f.close()

        lif2 = sum(1 for line in open('userInputAi'))       # gets number of lines in this file
        f5 = open('userInputAi','r')
        frl2 = f5.readlines()
        f5.close()

        lif3 = sum(1 for line in open('nxTopic'))       # gets number of lines in this file
        f6 = open('nxTopic','r')
        frl3 = f6.readlines()
        f6.close()

	for i in frl:
		list.append(i)				# create list of lines
	for i in frl2:
		list2.append(i)				# create list of lines
	while True:
		rnd1 = random.randint(0,(lif-1))	# Pick something random to say from the list
		rnd2 = random.randint(0,10)
		rnd3 = random.randint(0,(lif2-1))	# Pick something random to say from the list
		picker = (rnd2%2)
		if rnd2 == 0:
			soci()
		else:
#			Lo = list[rnd1]
			Lo = list2[rnd3]
			Lo = Lo.strip('\n')
			func4(Lo)				# Say this
			f = open('respondAi','r')
			frl = f.readlines()
			f.close()
			f2 = open('userInputAi','r')
		        frl2 = f2.readlines()
	#	        cnt = 0
		        f2.close()
		        v = func2()				# Get User Input
			if v == None:
				tmo = func5()
				if tmo == True:
					break

			elif v == 'bye' or v == 'Bye' or v == 'see ya':
				st = 'Ok, see ya =)'
				func4(st)
				sys.exit()
			try:
				v += '\n'
				while True:
				        line = frl2.index(v)
					break
			except:
				try:
					line2 = frl.index[line]
				        func4(line2) # Say this
					v = func2()
				except:
					try:
						line3 = frl3.index[line]
						continue
					except:
					        func3(v)

#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****
#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****#####*****

def main():
	global debug
	func1()
##########################################################################################################################################
##########################################################################################################################################

main()
