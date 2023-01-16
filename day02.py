# number = 0x9A
# print(number)
# number = 0o232
# print(number)
#
# print(bin(number))
# print(hex(number))
# print(oct(number))

int('10',2) #binary
int('10',22) #chester..

vowels = 'aeiou'
letter = 'u'
if letter in vowels:
    print(letter,'is a bowel')

tweet_string = "blah" * 50
tweet_limit = 20
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print(tweet_string)
else:
    print('went over by',abs(diff))
