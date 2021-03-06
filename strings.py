def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    string=''
    for word in vocab_words:
        if word==vocab_words[0]:    
            string =word
        else:
            string += (' :: ' + vocab_words[0] + word)
    return string


def remove_suffix_ness(word):
    if word[-5] == 'i':
        return word[:-5] + 'y'
    else:
        return word[:-4]


def adjective_to_verb(sentence, index):
    sentence_without_dot = sentence[:-1]
    list = sentence_without_dot.split()
    return list[index] + 'en'