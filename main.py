def main(): 
  path = "books/frankenstein.txt"
  book_text = read_book(path)
  total_words = count_words(book_text)
  total_letters = count_letters(book_text)
  character_dict  = ch_dict(total_letters)
  character_dict.sort(reverse=True, key=sort_on)
  print_report(total_words, character_dict)

def read_book(path): 
  with open(path) as f: 
    return f.read()

def count_words(text): 
  return len(text.split())

def count_letters(text): 
  lowercase_text = text.lower()
  dict = {}
  for char in lowercase_text: 
    if char in dict: 
      dict[char] += 1
    else: 
      dict[char] = 1
  return dict


def ch_dict(dict): 
  characters = []
  for ch in dict: 
    characters.append({"ch": ch, "num": dict[ch]})
  return characters

def sort_on(dict): 
  return dict["num"]

def print_report(total_words, character_dict):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{total_words} words found in the document")
  print()

  for ch_dict in character_dict: 
    if ch_dict["ch"].isalpha(): 
      print(f"The '{ch_dict["ch"]}' was found {ch_dict["num"]} times")

  print("---End report---")

main()