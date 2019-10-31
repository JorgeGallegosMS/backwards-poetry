def lines_printed_backwards(string_list):
    '''Takes in a list of strings containing the lines 
        of your poem and prints the lines in reverse
    '''
    index = len(string_list)
    string_list.reverse()
    for line in string_list:
        print(f"{index} {line}")
        index -= 1

poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''

lines_printed_backwards(poem.split("\n"))