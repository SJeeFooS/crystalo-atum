# Crystallite Size Calculator
## Description
The Crystallite Size Calculator is a graphical user interface (GUI) application that calculates the crystallite size and microstrain based on user-provided values of 2Theta and Half Width at Half Maximum (HWHM) (the half of FWHM can be obtained from fityk). It uses fundamental equations in crystallography to derive these parameters.

## Features
User-friendly interface to input 2Theta and HWHM values.
Calculation of Crystallite Size (CS) and Microstrain (Eta) for each peak.
Displays input values, intermediate calculations, and final results in a text box.
Installation

## Requirements
The application requires the following Python libraries:

numpy: >= 1.20.0
tkinter: (comes with Python standard library)

## Setup
1. Clone the repository or download the source code.

2. Ensure you have Python installed (Python 3.x).

3. Install the required packages by running:
``` bash
pip install numpy
```
# Usage

1. Run the application using the following command:

``` bash
python crystallite_size_calculator.py
````
2. Enter the 2Theta values (in degrees) and HWHM values (separated by spaces) in their respective input fields.
3. Click the Calculate button to compute the results.
4. View the results in the textbox below the button.

## Example Input

Theta values (degrees):
20 25 30
HWHM values: 
0.1 0.2 0.15
