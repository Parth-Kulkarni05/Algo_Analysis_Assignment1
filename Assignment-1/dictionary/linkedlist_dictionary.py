from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = None
        self.length = 0
        # TO BE IMPLEMENTED

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        prev = None

        for i in words_frequencies:
            new_node = WordFrequency(i.word, i.frequency)

            if self.head is None:
                self.head = new_node
                self.length = self.length + 1
                self.head.next = None

            else:
                cur_node = self.head

                for i in range(self.length - 1):
                    cur_node = cur_node.next
                
                cur_node.next = new_node
                new_node.next = None
                self.length = self.length + 1                                    

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        cur_node = self.head

        while cur_node is not None:
            if cur_node.word == word:
                return cur_node.frequency
            
            cur_node = cur_node.next

        return 0

        # TO BE IMPLEMENTED

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        cur_node = self.head
        new_node = WordFrequency(word_frequency.word, word_frequency.frequency)

        for i in range(self.length):

            if cur_node.word == word_frequency.word:
                return False
            
            elif cur_node.next is None:
                cur_node.next = new_node
                new_node.next = None

                self.length = self.length + 1
            
            cur_node = cur_node.next 
        
        return True
        
        # TO BE IMPLEMENTED
      

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        
        cur_node = self.head
        prev = None


        while cur_node is not None:
            if cur_node.word == word and cur_node == self.head:
                self.m_head = cur_node.next
                cur_node = None
                return True
            
            elif cur_node.word == word:

                prev.next = cur_node.next

                cur_node = None

                return True

            prev = cur_node
            cur_node = cur_node.next
        

        return False
        


        # TO BE IMPLEMENTED


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        '''
        
        So iterate through the linked list find the biggest frequency value 

        Then store the word of that frequency value 

        Then iterate again but if it's that word ignore it 

        Loop these 3 times and you got the biggest value.

        
        '''

        list_of_words = []

        cur_node = self.head

        for i in range(self.length - 1):
            if cur_node.word.startswith(word):
                if len(list_of_words) == 0:
                    list_of_words.append(cur_node)
                else:
                    for j in range(len(list_of_words)):
                        if cur_node.frequency > list_of_words[j].frequency:
                            list_of_words.insert(j, cur_node)
                            break

                        
            cur_node = cur_node.next
            

        # TO BE IMPLEMENTED
        return list_of_words[0:3]



