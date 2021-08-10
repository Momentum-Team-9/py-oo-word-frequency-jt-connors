import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read_contents(self):
        with open(self.filename) as poem:
            text = poem.read().lower()
            return text
        """
        This should read all the contents of the file
        and return them as one string.
        """
        #raise NotImplementedError("FileReader.read_contents")


class WordList:
    def __init__(self, text):
        self.text = text
        
    def extract_words(self):
        new_text = self.text.split()
        #print(new_text)
        for word in new_text:
            list = word.translate(str.maketrans("", "", string.punctuation))
            print(list)

        
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        #raise NotImplementedError("WordList.extract_words")

    def remove_stop_words(self):
        pass
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        #raise NotImplementedError("WordList.remove_stop_words")

        def get_freqs(self):
            pass
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        #raise NotImplementedError("WordList.get_freqs")


class FreqPrinter:
    def __init__(self, freqs):
        pass

    def print_freqs(self):
        pass
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
        #raise NotImplementedError("FreqPrinter.print_freqs")


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
