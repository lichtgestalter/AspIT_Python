"""
Exercise "Morris The Miner"

Copy this file into your own solution directory. Write your solution into the copy.

Initial situation:
Morris has the attributes sleepiness, thirst, hunger, whisky, gold.
All attributes have the starting value 0.
If sleepiness, thirst or hunger goes above 100, Morris the miner dies.
Morris can’t store more than 10 bottles of whisky.
Sleepiness, thirst, hunger do not go below 0.
Morris can't shop or eat without enough gold.

Possible moves for a turn:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Your task:
Write a program that gets Morris as much gold as possible in 1000 turns.

if you have no idea how to begin, open S0031.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).

when your program is complete, push it to your github repository
then send this Teams message to your teacher: i am done with exercise "Morris The Miner"
thereafter go on with the next file in numerical order in the teacher's exercise repository after the current exercise.
"""