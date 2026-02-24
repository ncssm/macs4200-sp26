def caesar(text, key, decrypt=False, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    
    final_text = ''

    for char in text:
        text_numerical = LETTERS.find( char )
        
        if decrypt:
            new_text_numerical = (text_numerical - key) % len(LETTERS)
        else:
            new_text_numerical = (text_numerical + key) % len(LETTERS)
        
        final_text += LETTERS[new_text_numerical]

    if decrypt:
        return final_text
    else:
        return final_text


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

def eea(k, m):
    """
    Returns the multiplicative inverse of k in modulus m. If no inverse exists, returns a ValueError
    """

    
    a, b = m, k
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    while b != 0:
        q = a // b
        a, x0, y0, b, x1, y1 = b, x1, y1, a - q*b, x0 - q*x1, y0 - q*y1 
    
    if a != 1:
        raise ValueError(f"Modular inverse does not exist for k = {k} and m = {m} (gcd = {a}).")

    return y0 % m
