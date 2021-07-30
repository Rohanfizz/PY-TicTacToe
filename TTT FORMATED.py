# -*- coding: utf-8 -*-
"""
@author: RohanSharma
"""


###############################################################################
#GLOBAL VARIABLES
yes = False
win = False

lturn=[1,2,3,4]
dboard=[11,7,11,10,11,8,11,10,11,9,11,'change',12,12,12,10,12,12,12,10,12,12,12,'change',11,4,11,10,11,5,11,10,11,6,11,'change',12,1,12,10,12,2,12,10,12,3,12]
p={11:'_',10:'|',12:' ',1:' ',2:' ',3:' ',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_',}

###############################################################################

def board():
	patterns={1:'___|___|___',2:'   |   |   ',3:'X',4:'O',5:' '}
	global dboard
	global p
	y=0
	line=[]
	for x in dboard:
		line.append(x)
		if len(line)%12==0:
			#print(pattern[x],end='')
			print(' ')
		else:
			#print(' ')
			print(p[x],end='')


###############################################################################

def yesno():
	start=str(input('Would you like to start the game? '))
	global yes
    
	if start.upper()=='YES':
		print('Okay!')
		yes=True
	else:
		yes=False
    

###############################################################################

def turn1():
	print(' ')
	p1 = int(input('Player1 its your turn: '))
	global p
	p[p1]='O'
	board()
	check()
	print(' ')
	
def turn2():
	p2=int(input('Player2 its your turn: '))
	p[p2]='X'
	board()
	check()
	print(' ')
	
###############################################################################

def check():
	global win

	if p[1]==p[2] and p[2]==p[3] and p[1]!=' ' and p[2]!=' ' and p[3]!=' ':
		win=True
	elif p[4]==p[5] and p[5]==p[6] and p[4]!='_' and p[5]!='_' and p[6]!='_':
		win=True
	elif p[7]==p[8] and p[8]==p[9] and p[7]!='_' and p[8]!='_' and p[9]!='_':
		win=True
	elif p[1]==p[4] and p[4]==p[7] and p[1]!=' ' and p[4]!='_' and p[7]!='_':
		win=True
	elif p[2]==p[5] and p[5]==p[8] and p[2]!=' ' and p[5]!='_' and p[8]!='_':
		win=True
	elif p[3]==p[5] and p[5]==p[9] and p[3]!=' ' and p[5]!='_' and p[9]!='_':
		win=True
	elif p[1]==p[5] and p[5]==p[9] and p[1]!=' ' and p[5]!='_' and p[9]!='_':
		win=True
	elif p[3]==p[5] and p[5]==p[7] and p[3]!=' ' and p[5]!='_' and p[7]!='_':
		win=True	
	else:
		win=False
	

	'''
	if (pattern[1]==pattern[2]==pattern[3]) or (pattern[4]==pattern[5]==pattern[6]) or (pattern[7]==pattern[8]==pattern[9]) or   (pattern[1]==pattern[4]==pattern[7]) or (pattern[2]==pattern[5]==pattern[8]) or (pattern[3]==pattern[6]==pattern[9]) or (pattern[1]==pattern[5]==pattern[9]) or (pattern[3]==pattern[5]==pattern[7]) and (pattern[1]!=' '):
	    win	=True
	else:
		win=False
	'''	
		

###############################################################################
def TicTacToe():
    
	yesno()

	global yes
	global win
	
	if yes==True:
		board()
		for t in lturn:
			turn1()
			check()
			if win==True:
				break
			
			print(' ')
			turn2()
			check()
			
			if win==True:
				break

		if win==True:
			print('YOU WON! GAME IS OVER')
			TicTacToe()
		if win==False:
			print('DRAW!')
			TicTacToe()
			
		
	
		

	else:
		print('GoodBye!')
		
	

###############################################################################
TicTacToe()




