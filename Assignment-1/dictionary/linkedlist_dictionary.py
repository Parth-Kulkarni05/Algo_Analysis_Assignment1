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
        # TO BE IMPLEMENTED

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        prev = None

        for i in words_frequencies:
            new_node = ListNode(i)

            if self.head is None:
                self.head = new_node
                self.head.next = None

            else:
                cur_node = self.head

                while cur_node.next:
                    cur_node = cur_node.next

                cur_node.next = new_node
                new_node.next = None     

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        cur_node = self.head

        while cur_node is not None:
            if cur_node.word_frequency.word == word:
                return cur_node.word_frequency.frequency
            
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
        new_node = ListNode(word_frequency)

        while cur_node.next is not None:

            if cur_node.word_frequency.word == word_frequency.word:
                return False
            
            cur_node = cur_node.next
            

        cur_node.next = new_node
        new_node.next = None

        
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
            if cur_node.word_frequency.word == word and cur_node == self.head:
                self.head = cur_node.next
                cur_node = None
                return True
            
            elif cur_node.word_frequency.word == word:

                prev.next = cur_node.next

                cur_node = None

                return True

            prev = cur_node
            cur_node = cur_node.next
        

        return False
        


        # TO BE IMPLEMENTED
    

    def bubble_sort(self, list_of_words):

        for k in range(0, len(list_of_words)):  
            for l in range(0, len(list_of_words)-k-1):  
                if (list_of_words[l].frequency < list_of_words[l + 1].frequency):  
                    temp = list_of_words[l]  
                    list_of_words[l] = list_of_words[l + 1]  
                    list_of_words[l + 1] = temp  
        

        return list_of_words[0:3]
    
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

        while cur_node is not None:
            if cur_node.word_frequency.word.startswith(word):
                    list_of_words.append(cur_node.word_frequency)
               
                        
            cur_node = cur_node.next
            

            list_of_words_sorted = self.bubble_sort(list_of_words)

        # TO BE IMPLEMENTED
        return list_of_words_sorted




