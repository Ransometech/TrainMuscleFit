

def main():
    text =input("Text: ")
    


def count_letters(text):
    count = 0
    for i in text:
        if i.isalpha():
            count +=1
    return count

def count_words(text):
    count +=0
    for i in text:
        if i == " ":
            count += 1

    return count +

def count_sentences(text):
    for i in text:
        if i in [".", "?", "!"]
        count += 1

    return count
