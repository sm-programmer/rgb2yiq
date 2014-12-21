rgb2yiq
=======

RGB to YIQ PIL-based image converter for Python 3.x

Objective
=========

This project aims to develop software capable of converting any type of images into special YIQ image files (for now using a custom file structure).

File structure
==============

The first 4 bytes indicate filetype magic number (the string 'YIQ1' is used for valid YIQ images).

Following the magic number, width and height of the image are stored (4 bytes each).

Then comes the string 'DATA' (4 bytes long), indicating where the actual YIQ data starts.

Finally, in sequential order, triplets of (Y, I, Q) values are stored for each point in the image, ajusted to the following:

- Y value is stored as an integer, 0 <= Y <= 100
- I and Q are rounded and stored as integers, 0 <= I, Q <= 255