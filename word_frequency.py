STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
import string
punctuation = string.punctuation
word_counts = {}

class FileReader:
    def __init__(self, filename):
        self.filename = filename



    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        opened_file = open(self.filename)
        self.opened_file = opened_file
        read_contents = (self.opened_file.read())
        self.read_contents = read_contents
        opened_file.close()
        #print (self.read_contents)
        return self.read_contents


class WordList:
    def __init__(self, text):
        self.text = text
        #print (self.text)
        #print ("was printed from inside the wordlist init")   
        #return self.text 
        """
        Apparently, return self.text is not necessary.  Discuss?  I'll offer up a possiblity.  The .text is an attribute of the object now.  It can be called from the following method without being passed in because it relates specifically to the "self" to which the next method will refer.  Is that right?  Or, is that maybe partly right?  Perhaps it will pass freely because it is still within the scope of the class WordList.  I say this because I noticed that the auto-fill wasn't working on variables anymore once I got down into the Printer class.  
        """

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        lower_case_text = (self.text.lower())
        #print (lower_case_text)
        no_hyphen = lower_case_text.replace("-", " ")
        #print (no_hyphen)
        no_punctuation = ""
        for char in no_hyphen:
            if char not in punctuation:
                no_punctuation = no_punctuation + char
        stripped_text = no_punctuation.strip()
        all_words = stripped_text.split()
        #print (all_words)
        #print ("printed from extract words post-split")
        self.all_words = all_words
             

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        #print (self.all_words)
        no_stop_words = []
        for word in self.all_words:
            if word not in STOP_WORDS:
                no_stop_words.append(word)
        #print (no_stop_words)
        self.no_stop_words = no_stop_words


    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        longest_word = 0
        for word in self.no_stop_words:
            if len(word) > longest_word:
                longest_word = len(word)
        self.longest = longest_word
        for word in self.no_stop_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        self.word_freqs_descending = (sorted(word_counts.items(), key=lambda seq: seq[1], reverse=True))
        print (self.word_freqs_descending)
        print (f" the longest word is {self.longest} characters long.")
        return self.word_freqs_descending, self.longest


class FreqPrinter:
    def __init__(self, freqs, longest):
        self.freqs = freqs 
        self.longest = longest
        print (self.longest)
        print ("printed inside the printer class")


    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """





if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
