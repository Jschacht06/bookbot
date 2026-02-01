def wordCount(text):
  text_splitted = text.split()
  total_words = len(text_splitted)
  return (total_words)

def count_unique(text):
  character_dictionary = {}
  count = 1
  lowered_text = text.lower()
  for char in lowered_text:
    if char == ' ':
      continue # ignoring whitespaces

    if char in character_dictionary:
      character_dictionary[char] +=1
    else:
      character_dictionary[char] = 1
  return character_dictionary

def sort_on(items):
  return items["num"]


def sortedList(character_dictionary):
  character_list = []
  for key in character_dictionary:
      character_list.append({"char": key , "num": character_dictionary.get(key)})
  character_list.sort(reverse=True, key=sort_on)
  return character_list