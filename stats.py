def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def get_num_words(text):
    number_of_words = text.split()
    return len(number_of_words)

def count_characters(text):
    count_map = {}
    for word in text:
        count_map[word.lower()] = count_map.get(word.lower(), 0) + 1
    return count_map

def sort_on(items):
    return items["num"]

def sort_characters(count_map):
    count_list = []
    for key, value in count_map.items():
        count_list.append({ "char": key, "num": value })
    count_list.sort(key=sort_on, reverse=True)
    return count_list

