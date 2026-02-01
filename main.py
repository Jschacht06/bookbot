import sys
from stats import wordCount , count_unique , sortedList
def main():
  print("Usage: python3 main.py <path_to_book>")
  book_path = sys.argv[1]
  
  text = get_book_text(book_path)

  totalWords = wordCount(text)
  charDict = count_unique(text)

  sorted_list = sortedList(charDict)
  #Report
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f" Found {totalWords} total words")
  print("--------- Character Count -------")
  for item in sorted_list:
    char = item.get('char')
    num = item.get('num')
    print(f"{char}: {num}")
  print("============= END ===============")

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents



main()