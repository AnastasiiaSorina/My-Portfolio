#Compulsory Task 2

sentence= '''The!quick!brown!fox!jumps!over!the!lazy!dog!.'''
sentence = sentence.replace("!", " ")
sentence_len = len(sentence) - 2
new_sentence = sentence[:sentence_len ] + sentence[sentence_len + 1:]
new_sentence = new_sentence.upper()
print(new_sentence)

#or

sentence= '''The!quick!brown!fox!jumps!over!the!lazy!dog!.'''
sentence_len = len(sentence) - 2
sentence = sentence[:sentence_len ] + sentence[sentence_len + 1:]
print(sentence.replace("!", " ").upper())