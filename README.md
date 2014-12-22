rgb2yiq
=======

RGB to YIQ PIL-based image converter for Python 3.x
Copyright (C) 2014	sm-programmer

Objective
=========

This project aims to develop software capable of converting any type of images into special YIQ image files (for now using a custom file structure).

YIQ files are interesting when it comes to obtaining compatible B/W images with no extra processing, whilst preserving colour information as well.

This small program demonstrates its usefulness as it only requires Pillow and a Python 3 interpreter to run properly.

How to use
==========

From a terminal, type the following:

python3 rgb2yiq inputimgfile.ext

It currently supports any image type supported by Pillow.

The program generates a file as output, named `inputimgfile.ext.yiq', with the structure described below.

File structure
==============

The first 4 bytes indicate filetype magic number (the string 'YIQ1' is used for valid YIQ images).

Following the magic number, width and height of the image are stored (4 bytes each).

Then comes the string 'DATA' (4 bytes long), indicating where the actual YIQ data starts.

Finally, in sequential order, triplets of (Y, I, Q) values are stored for each point in the image, ajusted to the following:

- Y value is stored as an integer, 0 <= Y <= 100
- I and Q are rounded and stored as integers, 0 <= I, Q <= 255

To Do
=====

1. Implement parameter-checks and a better parameter management system.
2. Generate output file to standard output for more flexibility.
3. Implement reverse-direction YIQ -> image file.

License
=======

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.