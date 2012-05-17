__author__ = 'thacdu'

def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in dic.iteritems() if v == val][0]

def find_value(dic, key):
    """return the value of dictionary dic given the key"""
    return dic[key]

GRADE_DICT = {
    'first': '1st Grade',
    'second': '2nd Grade',
    'third': '3rd Grade',
    'fourth': '4th Grade',
    'fifth': '5th Grade',
    'sixth': '6th Grade',
    'seventh': '7th Grade',
    'eighth': '8th Grade',
    'ninth': '9th Grade',
    'tenth': '10th Grade',
    'eleventh': '11th Grade',
    'twelfth': '12th Grade',
    'college': 'College',
    'other': 'Other',
    }

SUBJECT_DICT = {
    'art': 'Art',
    'bae': 'Business & Economics',
    'cos': 'Computer Science',
    'geo': 'Geography',
    'gov': 'Government & Politics',
    'his': 'History',
    'mat': 'Math',
    'mus': 'Music',
    'fol': 'Foreign Language',
    'sci': 'Science',
    'peh': 'PE & Health',
    'rel': 'Religion',
    'oth': 'Other',
    }