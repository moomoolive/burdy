def word_recognizer_and_position(text):
    position_count = 0
    current_word = 'blank'
    word_start_positions = []
    opinion_splitters = ["but", "although", "except", "<br>"]

    for i in range(len(text)):
        if text[i] == ' ':
            for word in opinion_splitters:
                if current_word == word:
                    word_start_position = position_count - len(word)
                    word_start_positions.append(word_start_position)

            current_word = 'blank'
        else:
            if current_word == 'blank':
                current_word = text[i].lower()
            else:
                current_word += text[i].lower()
        
        position_count += 1

    return word_start_positions,text

def parse_sentence_token(parse_position, text):
    number_of_parses = len(parse_position)
    
    parsed_sentence = []
    first_token = text[0: parse_position[0]]
    parsed_sentence.append(first_token)
        
    for i in range(number_of_parses):
        temporary_variable_1 = parse_position[i]

        if i + 1 == number_of_parses:
            temporary_variable_2 = None
        else:
            temporary_variable_2 = parse_position[i+1]
            
        temporary_list =  text[temporary_variable_1:temporary_variable_2]
        parsed_sentence.append(temporary_list)
    
    return parsed_sentence

def opinion_unit_creator(sentence_tokens):
    updated_sentence_token = []

    for sentence in sentence_tokens:
        splitting_words = word_recognizer_and_position(sentence)

        if len(splitting_words[0]) > 0:
            opinion_units = parse_sentence_token(splitting_words[0],splitting_words[1])
            updated_sentence_token.extend(opinion_units)
        else:
            updated_sentence_token.append(splitting_words[1])

    return updated_sentence_token