message = input("Enter the English message to translate into Pig Latin: ").split(" ")

def separate_non_letters(p_word):
    beg_nonletters = ""
    end_nonletters = ""
    while len(p_word) > 0 and  not p_word[0].isalpha():
	      beg_nonletters += p_word[0]
	      p_word = p_word[1:] 
    if len(p_word) == 0:
	      result.append(beg_nonletters)
	      return (beg_nonletters, end_nonletters, p_word)	      
    while not p_word[-1].isalpha():
	      end_nonletters += p_word[-1]
	      p_word = p_word[:-1]
    end_nonletters =  end_nonletters[::-1]  
    return (beg_nonletters, end_nonletters, p_word)

def convert_to_pig_latin(p_word):
    if p_word[0] in 'aeiouAEIOU':
        if p_word[0] == p_word[0].upper():
            p_word = p_word[0].upper() + p_word[1:] + 'yay'
        else:
            p_word = p_word + 'yay'
    else:
        if p_word[0] == p_word[0].upper():
            p_word = p_word[1].upper() + p_word[2:] + p_word[0].lower() +'ay'
        else:
            p_word = p_word[1:]+p_word[0]+'ay'
    return p_word

for word in message:
    result = []
    beg_nonletters, end_nonletters, word = separate_non_letters(word)
    word = beg_nonletters+convert_to_pig_latin(word)+end_nonletters
    result.append(word)        
    print(' '.join(result),  end=" ")
