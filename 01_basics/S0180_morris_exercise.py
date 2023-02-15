"""
Exercise "Morris The Miner":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Initial situation:
Morris has the attributes sleepiness, thirst, hunger, whisky, gold.
All attributes have the starting value 0.

Rules:
If sleepiness, thirst or hunger goes above 100, Morris the miner dies.
Morris can’t store more than 10 bottles of whisky.
No attribute may go below 0.

At each turn, Morris can perform exactly one of these activities:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Your task:
Write a program that gets Morris as much gold as possible in 1000 turns.

if you have no idea how to begin, open S0185_morris_help.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
