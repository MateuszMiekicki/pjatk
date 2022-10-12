import helper
import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def dtm():
    docs = [helper.read_file('article1.txt'), helper.read_file(
        'article2.txt'), helper.read_file('article3.txt')]
    vec = CountVectorizer()
    return pandas.DataFrame(vec.fit_transform(docs).toarray(), columns=vec.get_feature_names())


def tf():
    first_sentence = helper.filter_sentence(
        helper.read_file('article1.txt').split(" "))
    second_sentence = helper.filter_sentence(
        helper.read_file('article2.txt').split(" "))
    third_sentence = helper.filter_sentence(
        helper.read_file('article3.txt').split(" "))
    total = set(first_sentence).union(
        set(second_sentence)).union(set(third_sentence))

    first_sentence_dict = helper.make_dict(total, first_sentence)
    second_sentence_dict = helper.make_dict(total, second_sentence)
    third_sentence_dict = helper.make_dict(total, third_sentence)

    tf_first = helper.compute_tf(first_sentence_dict, first_sentence)
    tf_second = helper.compute_tf(second_sentence_dict, second_sentence)
    tf_third = helper.compute_tf(third_sentence_dict, third_sentence)

    return pandas.DataFrame([tf_first, tf_second, tf_third])

def tfidf():
    docs = [helper.read_file('article1.txt'), helper.read_file(
        'article2.txt'), helper.read_file('article3.txt')]
    vec = TfidfVectorizer()
    return pandas.DataFrame(vec.fit_transform(docs).toarray(), columns=vec.get_feature_names())

def main():
    print('dtm-------------------------')
    print(dtm())
    print('tf-------------------------')
    print(tf())
    print('tfidf-------------------------')
    print(tfidf())

main()
