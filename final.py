letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", ".", ",", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/", ".-.-.-", "--..--", "..--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

def translate(sentence):
    new_sentence = ""
    new_word = ""

    if is_it_code(sentence) == True:
        for i in range(len(sentence)):
            if sentence[i] != " ":
                new_word += sentence[i]
            else:
                for n in range(len(code)):
                    if code[n] == new_word:
                        new_sentence += letters[n]
                new_word = ""
        for n in range(len(code)):
                    if code[n] == new_word:
                        new_sentence += letters[n]

    elif is_it_code(sentence) == False:
        for i in range(len(sentence)):
            for n in range(len(letters)):
                if sentence[i] == letters[n]:
                    new_sentence += (code[n] + " ")

    else:
        new_sentence = is_it_code(sentence)

    return new_sentence



def is_it_code(sentence):
    is_code = False
    new_word = ""
    q = 0

    if sentence[0] in code:
        while sentence[q] != " ":
            new_word += sentence[q]
            q += 1
        if new_word in code:
            return True
        else:
            return "Error (not code or letters)"

    elif sentence[0] in letters:
        for i in range(len(sentence)):
            if i not in letters:
                return False
            else:
                return "Error (not code or letters)"

def letter_translator():
    for i in range(len(letters)):
        print letters[i] + " = " + code[i]

letter_translator()
print (is_it_code(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
print (translate(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
print (translate("hello world"))
print (translate("hello, world?"))
print (translate(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. ..--.."))
print (translate("my volleyball number is 17."))
print (translate("-- -.-- / ...- --- .-.. .-.. . -.-- -... .- .-.. .-.. / -. ..- -- -... . .-. / .. ... / .---- --... .-.-.-"))
print "Type what you want to translate!"
print (translate(raw_input("> ")))
