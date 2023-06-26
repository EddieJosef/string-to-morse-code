# String to Morse Code Application

This repository contains a Python script that converts strings to Morse code and vice versa. The script allows users to input text and obtain the corresponding Morse code representation, or input Morse code and obtain the corresponding text. The application supports the English alphabet, numbers, and some special characters.

## Project Overview

The String to Morse Code Application is a simple command-line tool that converts text to Morse code and vice versa. The script prompts the user to choose between coding (text to Morse code) or decoding (Morse code to text) and then prompts for the input accordingly. The conversion is performed using predefined lists that map each character to its respective Morse code representation.

## Features

The String to Morse Code Application offers the following features:

1. **Text to Morse Code Conversion**: Users can choose the "code" option and enter their desired text. The application then converts the text to Morse code using the International Morse Code standard and displays the result.

2. **Morse Code to Text Conversion**: Users can choose the "decode" option and enter Morse code. The application then converts the Morse code to text and displays the result.

3. **Input Validation**: The application checks the user's input for validity and handles invalid input gracefully. It ensures that only valid characters are used for conversion.

4. **Case Insensitivity**: The application handles both uppercase and lowercase letters in the input, converting them to their respective Morse code or text representations.

5. **Continuous Conversion**: After each conversion, the application prompts the user to choose another operation, allowing for multiple conversions without exiting the script.

## Usage

1. Clone the repository to your local machine or download the source code.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script `string_to_morse_code.py` using Python.

4. The script will prompt you to choose between "code" (text to Morse code) or "decode" (Morse code to text).

5. Enter your choice by typing "code" or "decode" and press Enter.

6. Depending on your choice, the script will prompt you to enter the text or Morse code you wish to convert.

7. Enter the input and press Enter.

8. The script will perform the conversion and display the result.

9. After displaying the result, the script will prompt you to choose another operation. Type your choice and press Enter to continue converting.

10. To exit the script, you can press Ctrl+C or close the terminal/command prompt.

## Limitations

The String to Morse Code Application has the following limitations:

- **Limited Character Set**: The application supports only the English alphabet (lowercase and uppercase), numbers from 0 to 9, and a few special characters (such as ".", ",", "?", and "'"). Other characters or non-English characters will be considered invalid input.

- **No Graphical Interface**: The application is a command-line tool and does not provide a graphical user interface (GUI). It is meant to be run from the terminal or command prompt.
