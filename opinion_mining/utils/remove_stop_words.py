from nltk.corpus import stopwords

# Remove stop words
stop_words = set(stopwords.words("english"))


def remove_stop_words(sentence):
    filtered_sentence = []

    for w in sentence:
        if w not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence
