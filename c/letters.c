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
    FILE *fp;
    fp = fopen(file_to_count, "r");

    if(fp == NULL) {
        printf("%s does not exist!", file_to_count);
        exit();
    }

    fclose(fp);
}