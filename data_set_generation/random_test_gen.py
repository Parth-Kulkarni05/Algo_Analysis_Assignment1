from calendar import c
from operator import not_
import random
import os
from pathlib import Path

p = Path(__file__).with_name('500output.txt')

choices = ['S']

test_amount_to_generated = int(input())

with open(p,'r') as test_1_500, open(f'test10.in','w') as outfile, open('Assignment-1\sampleData200k.txt') as addWords:
     word_list = [r.split() for r in test_1_500]
     not_in_list = [word.split() for word in addWords]

     word_list = word_list[0: test_amount_to_generated]
     random.shuffle(not_in_list)
     
     for i in word_list:
          selection = random.randint(0,1)
          choice = random.choice(choices)

          if choice =='A' and selection == 1:
               for k in not_in_list:
                  outfile.write(str(choice) + " " + k[0] + " " + k[1])
                  outfile.write('\n')
                  random.shuffle(not_in_list)
                  break
          
          elif choice == 'A' and selection == 0:
               outfile.write(str(choice) + " " + i[0] + " " + i[1])
               outfile.write('\n')
          
          elif choice == 'S' and selection == 1:
               for k in not_in_list:
                  outfile.write(str(choice) + " " + k[0])
                  outfile.write('\n')
                  random.shuffle(not_in_list)
                  break

     
          else:
               outfile.write(str(choice) + " " + i[0])
               outfile.write('\n')

