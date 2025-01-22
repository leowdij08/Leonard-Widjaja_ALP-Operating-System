import random

def extra():
    print("""
\033[1;34mList of extra commands:\033[0m
\033[1;33m• tree:\033[0m show the directory tree.
\033[1;33m• size [file/directory]:\033[0m size of a file or directory.
\033[1;33m• calc [expression]:\033[0m kalculator.
\033[1;33m• spongebob:\033[0m spongebob.
\033[1;33m• joke:\033[0m jokes.
""")

def joke():
    jokes = [
        "\nWhy did the developer go broke? Because he used up all his cache!\n",
        "\nWhy don’t programmers like to go outside? Because they’d rather loop through life.\n",
        "\nWhy do Python programmers wear glasses? Because they can’t find their C.\n",
        "\nWhat’s a programmer’s favorite type of music? Algo-rhythms.\n",
        "\nWhy did the programmer stay calm during the error? Because he had a try-catch block ready!\n",
        "\nWhy don’t keyboards ever get tired? They have built-in shortcuts!\n",
        "\nWhat’s a computer’s favorite snack? Microchips, but they can’t have just one byte!\n",
        "\nWhy was the website so good at its job? It had great domain knowledge!\n",
        "\nWhy did the programmer get a promotion? He had the perfect class!\n",
        "\nHow do you comfort a JavaScript bug? You console it.\n",
    ]
    selected_jokes = random.choice(jokes)
    print(selected_jokes)

spongebob_art = r"""
⠀⠀⠀⠀⠀.--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)
"""

def spongebob():
    print(spongebob_art)

intro = r"""
     .-"-,
    /_ _  \
    \@ @  /
    (_= _)
      `)(_
      \__(/-"
     __|||__
    ((__|__))

Hello! Type "help" to get the list of commands available"""
"""> type \033[1;32mhelp\033[0m to see all the commands"""


outro = """
        .-"-.
       /  - -\
       \  @ @/
        (_ <_)
        _)(`
    ,_(`_))
     "-\)__/
      __|||__
     ((__|__))"""

outrotext = r"""Bye-bye"""
