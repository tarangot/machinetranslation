'''
translator module for final project

Author: Thomas Tarango
Date: July 5th, 2023
'''


from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''
    translates an English string to French

    Precondition: parameter english_text must be of type str and an English sentence
    Parameter english_text: the string to convert
    '''
    french_text = MyMemoryTranslator(source='english us', target='french').translate(english_text)
    return french_text


def french_to_english(french_text):
    '''
    translates an French string to English

    Precondition: parameter french_text must be of type str and a French sentence
    Parameter french_text: the string to convert
    '''
    english_text = MyMemoryTranslator(source='french', target='english us').translate(french_text)
    return english_text
