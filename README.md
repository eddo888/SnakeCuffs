# help on python c binding

# dependencies

install python3.8 from python.org

```bash
pip3 install pybind11
pip3 install invoke
pip3 install Cython
```

# security block
mac mojave blocks relative pathed libraries, here is the fix

[install_name_tool](https://stackoverflow.com/questions/33281753/unsafe-use-of-relative-rpath-libboost-dylib-when-making-boost-python-helloword-d)
```python
def install_name_tool(dependent=None, depends=[]):
    '''
    make the lib full path to get around security blocking relative paths
    '''
    for dependson in depends:
        full_path = os.path.abspath(dependson)
        shell_str='install_name_tool -change {0} {1} {2}'.format(dependson, full_path, dependent)
        print('    install_name_tool: {0}'.format(dependson))
        invoke.run(shell_str)
```


# mac G++ missing symbols
mac compile gets upset about missing symbols

[ignore missing symbols on a mac](https://pybind11.readthedocs.io/en/stable/compiling.html)
```html
On Mac OS: the build command is almost the same but it also requires passing the -undefined dynamic_lookup flag so as to ignore missing symbols when building the module:
```

## in task.py
```python
def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3.8-config --includes` "
        "`python3 -m pybind11 --includes` "
        "-undefined dynamic_lookup "
        "-I . "
        "{0} "
        "-o {1}`python3.8-config --extension-suffix` "
        "-L. -lcppmult -Wl,-rpath,.".format(cpp_name, extension_name)
    )
```


# compile and test
here is the output from a good compile and test run

```bash
$ invoke all
==================================================
= Building C Library 
* Complete
==================================================
= Testing ctypes Module 
    In cmult : int: 6 float 2.3 returning  13.8
    In Python: int: 6 float 2.3 return val 48.0

    In cmult : int: 6 float 2.3 returning  13.8
    In Python: int: 6 float 2.3 return val 13.8
==================================================
= Building CFFI Module 
    install_name_tool: libcmult.so
* Complete
==================================================
= Testing CFFI Module 
    In cmult : int: 6 float 2.3 returning  13.8
    In Python: int: 6 float 2.3 return val 13.8
==================================================
= Building C++ Library 
    install_name_tool: libcmult.so
    install_name_tool: cffi_example.cpython-38-darwin.so
* Complete
==================================================
= Building PyBind11 Module 
    install_name_tool: libcmult.so
    install_name_tool: cffi_example.cpython-38-darwin.so
    install_name_tool: libcppmult.so
* Complete
==================================================
= Testing PyBind11 Module 
    In cppmul: int: 6 float 2.3 returning  13.8
    In Python: int: 6 float 2.3 return val 13.8
==================================================
= Building Cython Module 
    install_name_tool: libcmult.so
    install_name_tool: cffi_example.cpython-38-darwin.so
    install_name_tool: libcppmult.so
* Complete
==================================================
= Testing Cython Module 
    In cppmul: int: 6 float 2.3 returning  13.8
    In Python: int: 6 float 2.3 return val 13.8

```

