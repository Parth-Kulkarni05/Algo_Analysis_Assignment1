import random

n_lines_to_be_generated = int(input("Enter the Number of Lines you want to Randomly Generate: "))

with open('Assignment-1\sampleData200k.txt') as dataPoint, open (f'data_set_generation\{n_lines_to_be_generated}output.txt','w') as outfile:

    word_list = [word.split() for word in dataPoint]

    random.shuffle(word_list) # The shuffle function randomly shuffles the list

    word_list = word_list[0: n_lines_to_be_generated]

    for i in word_list:
       outfile.write(i[0] + " " + i[1])
       outfile.write('\n')


print("File Generation Successful")