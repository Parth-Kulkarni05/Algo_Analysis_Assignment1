from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()
        # TO BE IMPLEMENTED

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        cur_node = self.root

        for word in words_frequencies:
            for letter in word.word:
                if letter not in cur_node.children:
                    cur_node.children[letter] = TrieNode(letter=letter, frequency=None, is_last=False)
                
                cur_node = cur_node.children[letter]

            # If it's the last letter of the word then do the following:

            cur_node.frequency = word.frequency
            cur_node.is_last = True 

            cur_node = self.root # Reset the cur_node variable by assigning it with self.root value
        

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED

        cur_node = self.root

        for letter in word:
            if letter not in cur_node.children:
                return 0
            cur_node = cur_node.children[letter]
        
        if cur_node.is_last:
            return cur_node.frequency
        
        else:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED

        cur_node = self.root

        word = word_frequency

        if self.search(word.word) == False:

            for letter in word.word:
                if letter not in cur_node.children:
                    cur_node.children[letter] = TrieNode(letter, frequency=None, is_last=False)

                cur_node = cur_node.children[letter] # If the letter is part of the children then move it there. 


            cur_node.frequency = word.frequency # If it's the last letter of the word then do the following:
            cur_node.is_last = True

            return True 
        
        
        return False
    


    def trie_explore_all_words(self, cur_node, previous_letter = '', list_of_words = []):

        if cur_node.is_last:
            word = previous_letter + cur_node.letter
            list_of_words.append(word)
        
        if len(cur_node.children.items()) !=0:
            for key, value in cur_node.children.items():
                self.trie_explore_all_words(value, previous_letter = previous_letter + cur_node.letter, list_of_words = list_of_words)
        

        return list_of_words

    



    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        if self.search(word):

            print(word)

            cur_node = self.root
            stack = []
            list_of_words = self.trie_explore_all_words(cur_node.children[word[0]], previous_letter='', list_of_words=[]) ## Adds all the words that start with word[0]
            list_of_prefixes = []

            for i in list_of_words:
                if i.startswith(word):
                    list_of_prefixes.append(i)
        

            
            ## If the word prefix list is more than one than just set the flag of that word to false or else really clean up the structure##

            if len(list_of_prefixes) > 1:
                for letter in word:
                    cur_node = cur_node.children[letter]
                
                cur_node.is_last = False
            
            else:

                cur_node = self.root

                stack = []

                for letter in word:
                    cur_node = cur_node.children[letter]
                    stack.append(cur_node)
                

                cur_node = self.root
                            
                
                if len(stack) == len(word) and len(stack) >= len(list_of_words):  ## So this assumes that there is only word within the trie that has been added

                    cur_node = self.root # Resets Cur_Node Position

                    del cur_node.children[word[0]] ## Delete by the first word so, everything afterwards is gone.
                    

                else: # So this assumes that the letters in the word we are deleting is used by other words added to the trie

                    # So start at the bottom, remove that last letter, come back up, and if that word is in the i of the list leave it. 
                    
                    reversed_stack = list(reversed(stack))

                    for i in range(1, len(reversed_stack)): # -1 so it does not go to the root
                        node = reversed_stack[i]

                        if i == 1:
                            for k in list(node.children.keys()):
                                if word.endswith(k):
                                    del node.children[k]
                        
                        else:
                            if len(node.children) == 1:
                                for k in list(node.children.keys()):
                                    if len(node.children[k].children) == 1:
                                        del node.children[k]
        

            return True
                
                            
        
        else:

            return False
                
    

            ## There are two cases here. Now it will be where we can delete up to a certain word because other words are using the letter
            ## We can check this by reffering to the is_last element



            ## If all nodes only have one children it's safe to assume we can completely remove them, so this means if the length of the word 
            # equals to the length of the list_of_words


        ## Just have to remove the word's end marker    


    def trie_explore(self,cur_node, previous_letter = '', prefix = '', d_list = []) -> [WordFrequency]:

        if cur_node.is_last: # This is the base case
            word = previous_letter + cur_node.letter

            if word.startswith(prefix):
                d_list.append(WordFrequency(word, cur_node.frequency))
                
        if len(cur_node.children.items()) !=0:                            
            for key, value in cur_node.children.items():
                    self.trie_explore(cur_node = value, previous_letter  = previous_letter + cur_node.letter, prefix = prefix, d_list = d_list)
        
        else:

            for k in range(0, len(d_list)):  # Once the
                for l in range(0, len(d_list)-k-1):  
                    if (d_list[l].frequency < d_list[l + 1].frequency):  
                        temp = d_list[l]  
                        d_list[l] = d_list[l + 1]  
                        d_list[l + 1] = temp  
            

        
        return d_list[0:3]



    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
    
        cur_node = self.root

        try:

            d_list = self.trie_explore(cur_node.children[word[0]], prefix= word, d_list=[])
            
            return d_list
        
        except:
            
            return []
