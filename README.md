# ASCII_ART-Python

This is a small program which converts an JPG/JPEG or any other format supported be Python's [Pillow](https://pillow.readthedocs.io/en/stable/) Image Library in RGB format.
This was part of the Robert Heaton's [**Programming Projects for Advanced Beginners**](https://robertheaton.com/2018/12/08/programming-projects-for-advanced-beginners/) blog post series.

## Methodology

	1. Load the Image
	2. Extract the Image RGB data as a 2-D Matrix
	3. Convert the Image RGB data to Brightness value using [AVERAGE] method: 
			brightness_of_pixel = ( R + B + G ) / 3
	4. Map each brightness value to the list of ASCII character list
	5. Print the ASCII Art.
	
