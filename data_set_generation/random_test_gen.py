import random
import os
from pathlib import Path

p = Path(__file__).with_name('100000output.txt')

choices = ['S']

with open(p,'r') as test_1_500, open(f'test10.in','w') as outfile, open('Assignment-1\sampleData200k.txt') as addWords:
     word_list = [r.split() for r in test_1_500]
     not_in_list = [word.split() for word in addWords]

     random.shuffle(word_list)
     random.shuffle(not_in_list)


     count = 0

     for i in range(15):
          count = count + 1
          selection = 1
          choice = random.choice(choices)

          if choice == 'S' and selection == 1 and count <= 3:
               for k in not_in_list:
                  outfile.write(str(choice) + " " + k[0] + " ")
                  outfile.write('\n')
                  random.shuffle(not_in_list)
                  break

     
          else:
               idx = random.randint(0,len(word_list))
               outfile.write(str(choice) + " " + word_list[idx][0] + " ")
               outfile.write('\n')
