# def square(number):
#     return number * number
#     # print(number * number)
# # by default a function returns the value none if we don't use "return" statement
#
#
# print(square(3))
#
# # exercise: emoji converter as a function:
#
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": '😁',
        ':(': '😔'
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


text = input('>')
output = emoji_converter(text)
print(output)

# --------------------------------------------------------------------------------

# def tarun(samplestring):
#     set
#     return [] + set
#     return samplestring + 'tarun'
#
#
# def nihas(samplestring):
#     ssample + element
#
#
# k = tarun('HI ')
# print(k)
# r = 'HIa '
# print(nihas(r))
# print(r)