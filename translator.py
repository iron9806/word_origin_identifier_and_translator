import sys
from googletrans import Translator



def main():
    raw_words = list_provider(sys.argv[1])
    TTrans(raw_words)



# fetches u all the words that are not english

def list_provider(the_file):
    translator = Translator()
    with open(the_file, "r") as the_file:

        pre_eng_words= []
        words = []

# itarates over the whole file , and appends all the words to the words[] list
        for line in the_file:
            for word in line.split():
                words.append(word.strip('",'))

#itarates over the "words" list and if a word is in any-other language, other than english, than it gets added to the 
#"pre_eng_words[]"  list        
        for de_word in words:
            detected = translator.detect(de_word)
            origin_lang = detected.lang
            if origin_lang != 'en':
                pre_eng_words.append(de_word)


        return pre_eng_words


# This is the actual translator function that translate the words provided by the "list_provider" function.

def TTrans(arg):
    translator = Translator()

    translated_texts = []
    
# list comprehension using "translate()" func from the googletrans library to translating the provided words .
    translated_list = [translator.translate(text, dest="en") for text in arg]
    
    for translation, src in zip(translated_list, arg):

        print(src, "  =  ", translation.text)

    


    
if __name__ == "__main__": 
    main()