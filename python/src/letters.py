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
               'P': 0, 'Q': 0, 'R': 0, 's':0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
               'X': 0, 'Y': 0, 'Z': 0}
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    i_count = 0
    j_count = 0
    k_count = 0
    l_count = 0
    m_count = 0
    n_count = 0
    o_count = 0
    p_count = 0
    q_count = 0
    r_count = 0
    s_count = 0
    t_count = 0
    u_count = 0
    v_count = 0
    w_count = 0
    x_count = 0
    y_count = 0
    z_count = 0

    PADDING = 6
    try:
        file = open(file_to_count, 'r')
        for line in file:
            letters['A'] += line.upper().count('A')
            a_count += line.upper().count('A')
            b_count += line.upper().count('B')
            c_count += line.upper().count('C')
            d_count += line.upper().count('D')
            e_count += line.upper().count('E')
            f_count += line.upper().count('F')
            g_count += line.upper().count('G')
            h_count += line.upper().count('H')
            i_count += line.upper().count('I')
            j_count += line.upper().count('J')
            k_count += line.upper().count('K')
            l_count += line.upper().count('L')
            m_count += line.upper().count('M')
            n_count += line.upper().count('N')
            o_count += line.upper().count('O')
            p_count += line.upper().count('P')
            q_count += line.upper().count('Q')
            r_count += line.upper().count('R')
            s_count += line.upper().count('S')
            t_count += line.upper().count('T')
            u_count += line.upper().count('U')
            v_count += line.upper().count('V')
            w_count += line.upper().count('W')
            x_count += line.upper().count('X')
            y_count += line.upper().count('Y')
            z_count += line.upper().count('Z')
        
        TOTAL_LETTERS = a_count + b_count + c_count + d_count + e_count + f_count + g_count + h_count + i_count + j_count 
        + k_count + l_count + m_count + n_count + o_count + p_count + q_count + r_count + s_count + t_count + u_count 
        + v_count + w_count + x_count + y_count + z_count

        
        print("RSTLNE")
        print("==========")
        print("R: {:5.2f}%".format(r_count/TOTAL_LETTERS * 100))
        print("S: {:5.2f}%".format(s_count/TOTAL_LETTERS * 100))
        print("T: {:5.2f}%".format(t_count/TOTAL_LETTERS * 100))
        print("L: {:5.2f}%".format(l_count/TOTAL_LETTERS * 100))
        print("N: {:5.2f}%".format(n_count/TOTAL_LETTERS * 100))
        print("E: {:5.2f}%".format(e_count/TOTAL_LETTERS * 100))
        print()

        print("VOWELS")
        print("==========")
        print("A: {:5.2f}%".format(a_count/TOTAL_LETTERS * 100))
        print("I: {:5.2f}%".format(i_count/TOTAL_LETTERS * 100))
        print("O: {:5.2f}%".format(o_count/TOTAL_LETTERS * 100))
        print("U: {:5.2f}%".format(u_count/TOTAL_LETTERS * 100))
        print()

        print("CONSONANTS")
        print("==========")
        print("B: {:5.2f}%".format(b_count/TOTAL_LETTERS * 100))
        print("C: {:5.2f}%".format(c_count/TOTAL_LETTERS * 100))
        print("D: {:5.2f}%".format(d_count/TOTAL_LETTERS * 100))
        print("F: {:5.2f}%".format(f_count/TOTAL_LETTERS * 100))
        print("G: {:5.2f}%".format(g_count/TOTAL_LETTERS * 100))
        print("H: {:5.2f}%".format(h_count/TOTAL_LETTERS * 100))
        print("J: {:5.2f}%".format(j_count/TOTAL_LETTERS * 100))
        print("K: {:5.2f}%".format(k_count/TOTAL_LETTERS * 100))
        print("M: {:5.2f}%".format(m_count/TOTAL_LETTERS * 100))
        print("P: {:5.2f}%".format(p_count/TOTAL_LETTERS * 100))
        print("Q: {:5.2f}%".format(q_count/TOTAL_LETTERS * 100))
        print("V: {:5.2f}%".format(v_count/TOTAL_LETTERS * 100))
        print("W: {:5.2f}%".format(w_count/TOTAL_LETTERS * 100))
        print("X: {:5.2f}%".format(x_count/TOTAL_LETTERS * 100))
        print("Y: {:5.2f}%".format(y_count/TOTAL_LETTERS * 100))
        print("Z: {:5.2f}%".format(z_count/TOTAL_LETTERS * 100))

    except FileNotFoundError:
        print(ARGS.file + " not found!")

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-f', '--file', dest='file', action='store')
    ARGS = PARSER.parse_args()
    count_letters(ARGS.file)
