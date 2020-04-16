#!/usr/bin/env python3

# ctypes_test.py
import ctypes, pathlib


#____________________________________________________________________________________________________
def main():
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "libcmult.so"
    c_lib = ctypes.CDLL(libname)

	x, y = 6, 2.3
	answer = c_lib.cmult(x, ctypes.c_float(y))
	print(answer)
	
	
#____________________________________________________________________________________________________
if __name__ == "__main__": main()
	
