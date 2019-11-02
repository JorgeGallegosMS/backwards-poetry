import random

def lines_printed_backwards(string_list):

    '''Takes in a list of strings containing the lines 
        of your poem and prints the lines in reverse'''

    index = len(string_list)
    string_list.reverse()
    for line in string_list:
        print(f"{index} {line}")
        index -= 1

def lines_printed_random(string_list):

    '''Randomly selects lines from a list of strings and 
        prints them out in random order'''
        
    lines = []

    for _ in range(0, len(string_list)):
        index = random.randint(0, len(string_list) - 1)
        lines.append(string_list[index])

    print("\n".join(lines))

def odd_lines_printed(string_list):
    '''Takes in a list of strings and prints only the
        odd numbered lines'''
    for index, line in enumerate(string_list):
        if (index + 1) % 2 == 1:
            print(f"{index + 1} {line}")

poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''.split("\n")

# lines_printed_backwards(poem)
# lines_printed_random(poem)
# odd_lines_printed(poem)