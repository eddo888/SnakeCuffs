
#include <stdio.h>
#include <stdlib.h>
#include "cmulti.h"

// cmult.c
float cmult(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("    In cmult : int: %d float %.1f returning  %.1f\n", int_param,
            float_param, return_value);
    return return_value;
}

int main (int argc, char **argv) {
  cmult(1, 1.2);
  exit(0);
}
