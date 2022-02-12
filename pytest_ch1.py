# write a function that takes a string argument
# and returns the number of vowels in it.
def vowel_count(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

print(vowel_count('hello'))
print(vowel_count('hello world'))
print(vowel_count('the quick brown fox jumped over the lazy brown dog'))
print(vowel_count('qwrtghbvx'))
print(vowel_count('0'))


def test_vowel_count(string):
    assert vowel_count('hello') == 2

def test_vowel_count_is_lowercase(string):
    assert vowel_count('HELLO') == 2

print(test_vowel_count('hello'))
print(test_vowel_count_is_lowercase('HELLO'))