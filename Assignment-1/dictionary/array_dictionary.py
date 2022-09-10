from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):

        self.array = []
        # TO BE IMPLEMENTED

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        for i in words_frequencies:
            self.array.append(WordFrequency(i.word, i.frequency))
        

        self.array.sort(key=lambda i: i.word)
    
    
   # TO BE IMPLEMENTED


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        for i in self.array:
            if i.word == word:
                return i.frequency
        
        return 0

        # TO BE IMPLEMENTED

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED

        if not self.search(word_frequency.word): # Word is not present in the dictionary
              for i in range(len(self.array)):
                if word_frequency.word < self.array[i].word:
                    self.array.insert(i,WordFrequency(word_frequency.word, word_frequency.frequency))
                    break 
        
        else:
            return False # Word is already in the dictionary
          
        
        return True
    


    def find_index(self,word):
        
        low_point = 0 
        high_point = len(self.array)
        mid_point = 0

        while low_point <= high_point:
            mid_point = (high_point + low_point) // 2

            if self.array[mid_point].word < word:
                low_point  = mid_point + 1
            
            elif self.array[mid_point].word > word:
                high_point = mid_point - 1
            
            else:
                return mid_point

        return 0



        

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED

        for i in self.array:
            if i.word == word:
                self.array.remove(i)
                return True
        
        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        list_of_words = []

        for i in range(len(self.array)):
            if self.array[i].word.startswith(prefix_word):
                list_of_words.append(self.array[i])
                
                for k in range(0, len(list_of_words)):  
                    for l in range(0, len(list_of_words)-k-1):  
                        if (list_of_words[l].frequency < list_of_words[l + 1].frequency):  
                            temp = list_of_words[l]  
                            list_of_words[l] = list_of_words[l + 1]  
                            list_of_words[l + 1] = temp  
        
        list_of_words = list_of_words[0:3]
    

        return list_of_words
