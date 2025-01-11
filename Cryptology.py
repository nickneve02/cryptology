abc = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
        11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

_123 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm':12, 'n':13, 'o': 14,
       'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def decode(message, offset): #decodes message with the offset input
    decoded = ''
    for char in message:
        if char == ' ' or char == '.' or char == '?' or char == '!' or char == ',' or char == '\'':
            decoded += char
        else:
            decoded += abc[(_123[char] + offset) % 26]
    return decoded

def encode(message, offset): #encodes a message to make it secret with an offset input
    encode = ''
    for char in message:
        if char == ' ' or char == '.' or char == '?' or char == '!' or char == ',' or char == '\'':
            encode += char
        else:
            encode += abc[(_123[char] - offset) % 26]
    return encode

def get_place_value(message):
    answer = []
    for char in message:
        if char == ' ' or char == '.' or char == '?' or char == '!' or char == ',' or char == '\'':
            answer.append(char)
        else:
            answer.append(_123[char])
    return answer

def keyword(message, key): #creates keyword phrase
    result = ''
    count = 0
    for i in range(len(message)):
        if message[i] == ' ' or message[i] == '.' or message[i] == '?' or message[i] == '!' or message[i] == ',' or message[i] == '\'':
            result += message[i]
            count += 1
        else:
            result += key[(i - count) % len(key)]
    return result

def get_offset(key, message):
    offset = 0
    answer = ''
    for i in range(len(message)):
        if message[i] == ' ' or message[i] == '.' or message[i] == '?' or message[i] == '!' or message[i] == ',' or message[i] == '\'':
            answer += message[i]
        else:
            offset = _123[message[i]]
            answer += decode(abc[key[i]], offset)
    return answer

def place_value(message, keyword): #Creates resulting place value
    result = []
    helper = 0
    for i in range(len(message)):
        if message[i] == ' ' or message[i] == '.' or message[i] == '?' or message[i] == '!' or message[i] == ',' or message[i] == '\'':
            result.append(message[i])
        else:
            helper = (_123[message[i]] - _123[keyword[i]])
            if helper < 0:
                result.append(26 - abs(helper))
            else:
                result.append(abs(_123[message[i]] - _123[keyword[i]])) #fix this
    #return final_result(result)
    return result

def final_result(result): #finds each letter from the place value 
    answer = ''
    for num in result:
        if num == ' ' or num == '.' or num == '?' or num == '!' or num == ',' or num == '\'':
            answer += num
        else:
            answer += abc[num]
    return answer

print('Hello, welcome to cryptology!')
is_true = True
while (is_true):
    type_of_crypt = input('Would you like to do a Caesar or Vigenere Cipher? ')
    en_or_de = input("Would you like to encode or decode? ")

    if type_of_crypt.lower() == 'vigenere':

        if en_or_de.lower() == 'decode': 
        #decode
            message = input("What is your message to decode? ")
            key = input("What is the key? ")
            place_value = get_place_value(message.lower())   
            keyword_phrase = keyword(message.lower(), key.lower())
            answer = get_offset(place_value, keyword_phrase)
            print(answer)

        elif en_or_de.lower() == 'encode':
        #encode
            message = input("What is your message to encode? ")
            key = input("What is the key? ")
            keyword_phrase = keyword(message.lower(), key.lower())    
            values = place_value(message.lower(), keyword_phrase)   
            final_answer = final_result(values)
            print(final_answer)

    elif type_of_crypt.lower() == 'caesar':

        if en_or_de.lower() == 'decode':
        #decode
            message = input("What is your message to decode? ")
            offset = int(input("What is the offset? "))
            answer = decode(message.lower(), offset)   
            print(answer) 

        elif en_or_de.lower() == 'encode':
        #encode
            message = input("What is your message to encode? ")
            offset = int(input("What is the offset? "))
            answer = encode(message.lower(), offset)
            print(answer)
    else:
        is_true = False

print("Thank you for trying cryptology!")
