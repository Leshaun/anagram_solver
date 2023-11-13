from nltk.corpus import words


def dictionary_by_length(word_list):
    words_by_length = {}
    for word in word_list:
        if len(word) in words_by_length:
            words_by_length[len(word)].append(word)
        else:
            words_by_length[len(word)] = [word]
    return words_by_length


def anagram_solver(sorted_dictionary):
    while True:
        anagram = input("Type exit to exit program.\nPlease enter your anagram: ")
        if anagram == "exit":
            break
        else:
            try:
                a = [i.lower() for i in anagram]
                output_words = []
                for w in sorted_dictionary[len(anagram)]:
                    s_w = [i.lower() for i in w]
                    if sorted(s_w) == sorted(a):
                        output_words.append("".join(s_w))
                print("Anagrams solutions:")
                for word in set(output_words):
                    print(word)
            except:
                print("Invalid anagram")


anagram_solver(dictionary_by_length(words.words()))
