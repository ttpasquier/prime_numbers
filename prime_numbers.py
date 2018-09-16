#!usr/bin/env python3
#coding:utf-8
from math import sqrt, ceil
etendue = input("Please type until what number you want to find prime numbers : ")
while True:
	try:
		etendue = int(etendue)
	except ValueError:
		etendue = input("Please type again, it must be an integer : ")
	else:
		break

limite = ceil(sqrt(etendue))
max_list = [n for n in range(2, etendue+1)]

for i in range(2, limite+1):
	diviseurs = [x for x in range(1, i+1) if i%x==0]
	if len(diviseurs) == 2:
		for nb in max_list:
			if nb % i == 0 and nb != i:
				max_list.remove(nb)

print(max_list)