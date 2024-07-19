

def main():
    text =input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentence = count_sentences(text)

    L = letters / words
    S = letters / words
    index = round(0.0588 * L - 0.296 * S -15.8)

    if index < 1:
        print("Before Grade 1")
    elif index>16:
        print("Grade 16+")
    else:
        print("Grade", index)

def count_letters(text):
    count = 0
    for i in text:
        if i.isalpha():
            count +=1
    return count

def count_words(text):
    count =0
    for i in text:
        if i == " ":
            count += 1

    return count + 1

def count_sentences(text):

    count =0
    for i in text:
        if i in [".", "?", "!"]:
            count += 1

    return count

main()
