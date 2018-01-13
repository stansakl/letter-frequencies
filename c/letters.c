/*
MIT License

Copyright (c) 2018 Stan Sakl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
#include <stdio.h>
#include "letters.h"

void main (int argc, char** argv) 
{
    if (argc <=1) {
        usage();
        exit();
    }
    printf("Parsing %s\n", argv[1]);
    count_letters(argv[1]);
}

void usage() {
    printf("Usage:\n");
    printf("\tletters <file name>\n");
}

void count_letters(char const *file_to_count) {
    int a_count = 0;
    int b_count = 0;
    int c_count = 0;
    int d_count = 0;
    int e_count = 0;
    int f_count = 0;
    int g_count = 0;
    int h_count = 0;
    int i_count = 0;
    int j_count = 0;
    int k_count = 0;
    int l_count = 0;
    int m_count = 0;
    int n_count = 0;
    int o_count = 0;
    int p_count = 0;
    int q_count = 0;
    int r_count = 0;
    int s_count = 0;
    int t_count = 0;
    int u_count = 0;
    int v_count = 0;
    int w_count = 0;
    int x_count = 0;
    int y_count = 0;
    int z_count = 0;
    
    FILE *fp;
    fp = fopen(file_to_count, "r");

    if(fp == NULL) {
        printf("%s does not exist!", file_to_count);
        exit();
    }

    fclose(fp);
}