# MIT License

# Copyright (c) 2018 Stan Sakl

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
""" Read a file of phrases and calculate the total letter frequency in the entire file."""
import argparse

def count_letters(file_to_count):
    """ Count the letters in each phrase, total them, and report percentage of occurrence for each. """

    letters = {'A': 0, 'B': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
               'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
               'P': 0, 'Q': 0, 'R': 0, 'S':0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
               'X': 0, 'Y': 0, 'Z': 0}
    try:
        file = open(file_to_count, 'r')
        for line in file:
            letters['A'] += line.upper().count('A')
            letters['B'] += line.upper().count('B')
            letters['C'] += line.upper().count('C')
            letters['D'] += line.upper().count('D')
            letters['E'] += line.upper().count('E')
            letters['F'] += line.upper().count('F')
            letters['G'] += line.upper().count('G')
            letters['H'] += line.upper().count('H')
            letters['I'] += line.upper().count('I')
            letters['J'] += line.upper().count('J')
            letters['K'] += line.upper().count('K')
            letters['L'] += line.upper().count('L')
            letters['M'] += line.upper().count('M')
            letters['N'] += line.upper().count('N')
            letters['O'] += line.upper().count('O')
            letters['P'] += line.upper().count('P')
            letters['Q'] += line.upper().count('Q')
            letters['R'] += line.upper().count('R')
            letters['S'] += line.upper().count('S')
            letters['T'] += line.upper().count('T')
            letters['U'] += line.upper().count('U')
            letters['V'] += line.upper().count('V')
            letters['W'] += line.upper().count('W')
            letters['X'] += line.upper().count('X')
            letters['Y'] += line.upper().count('Y')
            letters['Z'] += line.upper().count('Z')

        TOTAL_LETTERS = letters['A'] + letters['B'] + letters['C'] + letters['D']
        + letters['E'] + letters['F'] + letters['G'] + letters['H']
        + letters['I'] + letters['J'] + letters['K'] + letters['L']
        + letters['M'] + letters['N'] + letters['O'] + letters['P']
        + letters['Q'] + letters['R'] + letters['S'] + letters['T']
        + letters['U'] + letters['V'] + letters['W'] + letters['X']
        + letters['Y'] + letters['Z']

        print("RSTLNE")
        print("==========")
        print("R: {:5.2f}%".format(letters['R']/TOTAL_LETTERS * 100))
        print("S: {:5.2f}%".format(letters['S']/TOTAL_LETTERS * 100))
        print("T: {:5.2f}%".format(letters['T']/TOTAL_LETTERS * 100))
        print("L: {:5.2f}%".format(letters['L']/TOTAL_LETTERS * 100))
        print("N: {:5.2f}%".format(letters['N']/TOTAL_LETTERS * 100))
        print("E: {:5.2f}%".format(letters['E']/TOTAL_LETTERS * 100))
        print()

        print("VOWELS")
        print("==========")
        print("A: {:5.2f}%".format(letters['A']/TOTAL_LETTERS * 100))
        print("I: {:5.2f}%".format(letters['I']/TOTAL_LETTERS * 100))
        print("O: {:5.2f}%".format(letters['O']/TOTAL_LETTERS * 100))
        print("U: {:5.2f}%".format(letters['U']/TOTAL_LETTERS * 100))
        print()

        print("CONSONANTS")
        print("==========")
        print("B: {:5.2f}%".format(letters['B']/TOTAL_LETTERS * 100))
        print("C: {:5.2f}%".format(letters['C']/TOTAL_LETTERS * 100))
        print("D: {:5.2f}%".format(letters['D']/TOTAL_LETTERS * 100))
        print("F: {:5.2f}%".format(letters['F']/TOTAL_LETTERS * 100))
        print("G: {:5.2f}%".format(letters['G']/TOTAL_LETTERS * 100))
        print("H: {:5.2f}%".format(letters['H']/TOTAL_LETTERS * 100))
        print("J: {:5.2f}%".format(letters['J']/TOTAL_LETTERS * 100))
        print("K: {:5.2f}%".format(letters['K']/TOTAL_LETTERS * 100))
        print("M: {:5.2f}%".format(letters['M']/TOTAL_LETTERS * 100))
        print("P: {:5.2f}%".format(letters['P']/TOTAL_LETTERS * 100))
        print("Q: {:5.2f}%".format(letters['Q']/TOTAL_LETTERS * 100))
        print("V: {:5.2f}%".format(letters['V']/TOTAL_LETTERS * 100))
        print("W: {:5.2f}%".format(letters['W']/TOTAL_LETTERS * 100))
        print("X: {:5.2f}%".format(letters['X']/TOTAL_LETTERS * 100))
        print("Y: {:5.2f}%".format(letters['Y']/TOTAL_LETTERS * 100))
        print("Z: {:5.2f}%".format(letters['Z']/TOTAL_LETTERS * 100))

    except FileNotFoundError:
        print(ARGS.file + " not found!")

def calculate_percentage(letter, total_letters):
    return letter/total_letters * 100

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-f', '--file', dest='file', action='store')
    ARGS = PARSER.parse_args()
    count_letters(ARGS.file)
