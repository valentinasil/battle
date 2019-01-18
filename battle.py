import time
import random

print()
print('-'*60)
print()

print('A whild rapidash appears')
time.sleep(0.3)
print('...the background music changes...')
time.sleep(0.3)
print('you only have one pokemon, seel')
time.sleep(0.3)
print('I choose you seel!!!')
time.sleep(0.3)
print()

#set the starting health values 
seel_hp= 250
rapidash_hp= 600

#display the current healths 
print('starting HP:')
time.sleep(0.3)
print('seel HP: ' + str(seel_hp))
time.sleep(0.3)
print('rapidash HP: ' + str(rapidash_hp))
time.sleep(0.3)
print()

while seel_hp > 0 and rapidash_hp > 0:

	time.sleep(0.3)
	print('-[1] punch👊')
	time.sleep(0.3)
	print('-[2] blow away🌬')
	time.sleep(0.3)
	print('-[3] Eat mango🍈')
	time.sleep(0.3)
	print('-[4] Rap battle🎤')
	time.sleep(0.3)
	print()

	player_move = input('pick a move using the corresponding number:')
	player_move= int(player_move)
	if player_move==1:
		rapidash_hp = rapidash_hp -25
		print('seel uses Tackle and deals 25 HP of damage.')
	elif player_move==2:
		damage= random.randint(5,40)
		rapidash_hp= rapidash_hp-damage 
		print('seel uses super Screech and deals'+ str(damage)+ 'HP of damage. ')
	elif player_move==3:
		seel_hp=seel_hp+100
		print('seel uses Eat leek amd recovers 100 Hp.')

	time.sleep(0.3)
	print()

	#enemy battle choices 
	Enemy_move= random.randint(1,2)
	if Enemy_move == 1:
		seel_hp= seel_hp-30
		print('wartortle uses water blast and deals 30 Hp of damage.')
	elif Enemy_move== 2:
		seel_hp = seel_hp-20
		rapidash_hp = rapidash_hp+20
		print('rapidash uses Dink blood and deals 20 Hp of damage')

	time.sleep(0.3)
	print()
	#check and avoid negative HP
	if seel_hp < 0:
		seel_hp = 0

	if rapidash_hp < 0:
		rapidash_hp= 0

	#display the correct healths 

	print('Update HP:')
	print('seel HP:' +str(seel_hp))
	print('rapidash HP:' +str(rapidash_hp))
	time.sleep(0.3)
	print()

#check your work
if seel_hp > 0 and rapidash_hp ==0:
	print('wild rapidash fainted. seel wins')
if seel_hp==0 and rapidash_hp==0:
	print('seel has fainted. wild rapidash wins')
	print('you have no remaining pokemon, you lose.')









