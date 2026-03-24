def text_clean(text, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    upper_case_text = text.upper()
    cleaned_text = ''
    
    for char in upper_case_text:
        if char in LETTERS:
            cleaned_text += char

    return cleaned_text

def text_block(text, n=5):
    blocked_text = ''
    counter = 0
    
    for char in text:
        blocked_text += char
        counter += 1
        if counter % 5 == 0:
            blocked_text += ' '
    
    return blocked_text.strip()

def vigenere(text, keyword, decrypt=False, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Arguments:
        text (str): either the plaintext or ciphertext to work with
        keyword (str): the primer / keyword that will be used to create the entire keystream
        decrypt (bool, optional): True --> decrypt the message, False --> encrypt the message
        LETTERS (str, optional): defines the alphabet of allowable characters
    Returns:
        (str): encrypted / decrypted version of message formatting to specifications
    """
    # BEGIN SOLUTION NO PROMPT

    cleaned_text = text_clean(text, LETTERS)
    keyword = text_clean(keyword, LETTERS)
    final_text = '' 

    for i in range(len(cleaned_text)):
        new_text_numerical = LETTERS.find( cleaned_text[i] )
        keyword_numerical = LETTERS.find( keyword[i % len(keyword)] )

        if decrypt:
            finaltext_number = (new_text_numerical - keyword_numerical) % len(LETTERS)
        else:
            finaltext_number = (new_text_numerical + keyword_numerical) % len(LETTERS)

        final_text += LETTERS[finaltext_number]

    if decrypt:
        return final_text.lower()
    else:
        return text_block(final_text)
    # END SOLUTION
