# Bookbot

Bookbot is a python tool that reads books in the form of txt files and reports back info like word count and character count

## Features

- **Word Count**: Automatically calculates the total number of words in any text document.
- **Character Frequency**: Analyzes and counts the occurrences of every character in the text.
- **Sorted Reporting**: Displays character counts in a clean, sorted list for easy analysis.

## Installation

1. Clone this repository to your local machine.
2. Create a folder named `books/` in the root directory to store your `.txt` files.

```bash
mkdir books
```

3. Add any book or text file you wish to analyze into the `books/` folder.

## Usage

To run the analysis, use the following command in your terminal, replacing `<path_to_book>` with the actual path to your file (e.g., `books/frankenstein.txt`):

```bash
python3 main.py <path_to_book>
```

### Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
 Found 75948 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
...
============= END ===============
```

## Project Structure

- **main.py**: The entry point of the application that handles user input and displays the final report.
- **stats.py**: Contains the logic for word counting and character count.
- **.gitignore**: Configured to ignore the `books/` directory and Python cache files.

## Credits

This app was created as part of [Boot.dev](https://boot.dev).