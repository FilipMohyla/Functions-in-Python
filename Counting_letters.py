song_lyrics = """Load up on guns, bring your friends
It's fun to lose and to pretend
She's over-bored and self-assured
Oh no, I know a dirty word
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello
With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto, an albino, a mosquito, my libido
Yeah, hey
I'm worse at what I do best
And for this gift I feel blessed
Our little group has always been
And always will until the end
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello
With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now,…"""

letter = input("Zadej písmeno, jehož počet chceš zjistit: ")

def count_letter(song_lyrics, letter):
    """This function counts number of letter(s) in given string"""
    
    founded_letters = song_lyrics.lower().count(letter)
    
    return founded_letters

result = count_letter(song_lyrics, letter)
print("Počet výskytu písmena", letter, "v textu je", result)