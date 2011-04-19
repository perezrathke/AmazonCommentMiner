'''
MinerMiscUtils.py

@author: garyturovsky
@author: alanperezrathke
'''

# Returns true if part of speech is a noun, false otherwise
def isNoun( partOfSpeech ):
    return partOfSpeech.startswith('NN')

# Returns true if part of speech is an adjective, false otherwise
def isAdj( partOfSpeech ):
    return partOfSpeech.startswith('JJ')

# Returns the label for this comment
def getCommentLabel( rawCsvCommentDict ):
    return (int(rawCsvCommentDict[ "Thumbs Up!" ]) or int(rawCsvCommentDict[ "Thumbs Down" ]))