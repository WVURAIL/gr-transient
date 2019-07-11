# GNURadio Out of Tree Modules

To install the gnuradio OOT modules, follow these steps:

1: create a build directory if it does not already exist. To check if it exists, type in ls while in the gr-detection repository. If build is not seen in the response, type `mkdir build` while in the gr-detection repository. Then type cd build/. If the directory already exists, type cd build/.

2:Once in the directory, type `cmake ../` Then type `make` and look for any error messages. If none, then type `sudo make install`
