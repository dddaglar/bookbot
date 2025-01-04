def read(filepath):
    with open(filepath) as f:
        book = f.read()
    
    start = "*** START OF THIS PROJECT GUTENBERG EBOOK FRANKENSTEIN ***"
    end= "*** END OF THIS PROJECT GUTENBERG EBOOK FRANKENSTEIN ***"
    start_idx = book.find(start)
    end_idx = book.find(end)

    if start_idx != -1 and end_idx != -1:
        book = book[start_idx +len(start):end_idx]

    return book

def wordcount(text):
    wordlist = text.split()
    return len(wordlist)

def charlist(text):
    lettermap = {}
    text = text.lower()
    for l in text:
        if not l.isalpha():
            continue
        elif l in lettermap:
            lettermap[l] += 1
        elif l not in lettermap:
            lettermap[l] = 1
    return lettermap
    



def main():
    book = read("books/frankenstein.txt")
    chars, words = charlist(book), wordcount(book)
    chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    print("Being report of books/frankenstein.txt")
    print(f"{words} found in the document")
    for char in chars:
        print(f"the {char[0]} character was found {char[1]} times")
    print("End report")



main()