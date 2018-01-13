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