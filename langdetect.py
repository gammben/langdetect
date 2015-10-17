#!/usr/bin/env python
#coding:utf-8
# Author: Alejandro Nolla - z0mbiehunt3r
# Purpose: Example for detecting language using a stopwords based approach
# Created: 15/05/13

import sys

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'



#----------------------------------------------------------------------
def _calculate_languages_ratios(text):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


#----------------------------------------------------------------------
def detect_language(text):
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.
    
    It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Most scored language guessed
    @rtype: str
    """

    ratios = _calculate_languages_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language



#if __name__=='__main__':

#    text = '''
#    Faça o download nas primeiras 48 horas do lançamento e ganhe um presente de boas-vindas!
#Junte-se aos Minions nas férias de uma vida toda! Veja um adorável (mas desastrado) Minion chamado Phil afundar acidentalmente um navio de cruzeiro inteiro, carregando com ele seus amigos Minions que estavam de férias. Para se redimir, Phil deve transformar uma ilha tropical deserta em um destino de férias perfeito. A Illumination Entertainment – os criadores do filme MINIONS – e a EA convidam você para ajudar Phil a construir seu paraíso Minion definitivo..
#    '''

#    language = detect_language(text)

 #   print language

fhand = open("phrases.txt")    
for line in fhand: 
    line = line.rstrip()   
    text = line
    language = detect_language(text)
    print language
