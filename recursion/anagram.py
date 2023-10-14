"""
File: anagram.py
Name: Sunny
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO: This program will find and print anagrams from user input.
    """
    ####################
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            final_lst = find_anagrams(s)
        print(len(final_lst), 'anagrams: ', final_lst)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    ####################


def read_dictionary():
    vocab_list = []
    with open(FILE, 'r') as f:
        for line in f:
            vocab_list.append(line.strip())
    return vocab_list


def find_anagrams(s):
    """
    :param s: str, the input vocab
    :return: final list found from vocab list
    """
    final_lst = []
    index_lst = []
    vocab_list = read_dictionary()
    find_anagrams_helper(s, "", final_lst, index_lst, vocab_list)
    return final_lst


def find_anagrams_helper(s, new_word, final_lst, index_lst, vocab_list):
    if len(s) == 0:
        if new_word in vocab_list:
            if new_word not in final_lst:
                print('Found: ' + new_word)
                final_lst.append(new_word)
                print('Searching... ')
    else:
        for i in range(len(s)):
            if i not in index_lst:
                # Choose
                new_word = new_word + s[i]
                index_lst.append(i)
                # Early stopping, explore
                if has_prefix(new_word, vocab_list):
                    find_anagrams_helper(s, new_word, final_lst, index_lst, vocab_list)
                # Un-choose
                new_word = new_word[:-1]
                index_lst.pop()


def has_prefix(sub_s, vocab_list):
    """
    :param sub_s: str, the word being searched
    :return: bool, decide if the program keep explore or not
    """
    for s in vocab_list:
        if s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
