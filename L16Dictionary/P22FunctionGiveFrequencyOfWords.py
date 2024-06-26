# Write a function named freq_to_words that accepts a list of words as argument. It should return a dictionary which has the following structure:
# key: frequency of words in the list
# value: list of all words that have the above frequency
# Sample input-output behaviour:
#             words                                                       freq_to_words(words)
# ['a', 'random', 'collection', 'a', 'another', 'a', 'random']      {1: ['another', 'collection'], 2: ['random'], 3: ['a']}
# ['one', 'two', 'three', 'one']                                    {1: ['three', 'two'], 2: ['one']}

def words_to_frequency(words):
    freq_dict = dict()
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 0
        freq_dict[word] += 1
    return freq_dict

def freq_to_words(words):
    freq_dict = words_to_frequency(words)

    result = dict()
    for word in freq_dict:
        freq = freq_dict[word]
        if freq not in result:
            result[freq] = [ ]
        result[freq].append(word)

    return result

words = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']
print(freq_to_words(words))