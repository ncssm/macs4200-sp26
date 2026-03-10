def text_clean(text, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ', match_case=False):
    
    if match_case == False:
        text = text.upper()
        
    clean_text = ''
    
    for char in text:
        if char in LETTERS:
            clean_text += char

    return clean_text


def text_block( text, n = 5 ):
    blocked_text = ''
    
    for character in text:
        if len(blocked_text.replace(' ', '') ) % n == 0 and len(blocked_text) != 0:
            blocked_text += ' '

        blocked_text += character
    
    return blocked_text

def ioc(text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    ic = 0
    for char in LETTERS:
        ic += (text.count(char) / len(text)) * ((text.count(char)-1) / (len(text)-1))

    return ic
