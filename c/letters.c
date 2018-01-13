#include <stdio.h>
#include "letters.h"

void main (int argc, char** argv) 
{
    if (argc <=1) {
        usage();
        exit();
    }

    for(int i = 0; i < argc; i++) {
        printf("%s\n", argv[i]);
    }
}

void usage() {
    printf("Usage:\n");
    printf("\tletters <file name>\n");
}