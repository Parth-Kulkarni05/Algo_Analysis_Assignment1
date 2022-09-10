import random
import os
from pathlib import Path

p = Path(__file__).with_name('100000output.txt')

choices = ['A']

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

          if choice == 'A' and selection == 1 and count <= 10:
               for k in range(len(not_in_list)):
                    if word_list[k][0] != not_in_list[k][0]:
                              outfile.write(str(choice) + " " + not_in_list[k][0] + " " + not_in_list[k][1])
                              outfile.write('\n')
                              random.shuffle(not_in_list)
                              break

                    else: # So its equal then do the following
                              random.shuffle(word_list)
                              continue


     
          else:
               idx = random.randint(0,len(word_list))
               outfile.write(str(choice) + " " + word_list[idx][0] + " " + word_list[idx][1])
               outfile.write('\n')
