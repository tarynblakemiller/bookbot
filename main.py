def main():
    number_of_words = 0
    with open('books/frankentstein.txt') as f:
        file_contents = f.read()
        number_of_words = len(file_contents.split())
        print(f"{number_of_words} words found in the document")

        char_count = count_characters(file_contents)
        # print("Character counts:", char_count)

        character_report(char_count);

def count_characters(file_contents):
    char_dict = dict()
    for char in file_contents.lower():
      if char.isalpha():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
  
def character_report(char_dict):
    for key, value in char_dict.items():
        print(f"The '{key}' character was found {value} times")


main()
