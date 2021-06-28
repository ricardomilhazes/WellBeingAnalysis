import string

# Converts the string to the automata alphabet
def convert_automata_alphabet(c):
    ax = ""
    if c.isalpha() or c.isnumeric():
        if c in string.ascii_lowercase:
            ax = "x"
        else:
            ax = "X"
    else:
        ax = "."
    return ax


def word_breaker(transitions, initial, accepting, s):
    state = initial
    state_b = initial
    ns = ""
    for c in s:
        ax = convert_automata_alphabet(c)
        state_b = state
        state = transitions[state][ax]
        # print(state)
        if (
            (state_b == 3 and state == 2)
            or (state_b == 3 and state == 1)
            or (state_b == 2 and state == 1)
            or (state_b == 4 and state == 1)
            or (state_b == 4 and state == 2)
        ):
            c = " " + c
        ns = ns + c

    # return ns, state in accepting
    return ns


def phrase_breaker(t):
    # automata definition
    dfa = {
        0: {"X": 1, "x": 2, ".": 4},
        1: {"X": 1, "x": 2, ".": 3},
        2: {"x": 2, "X": 1, ".": 3},
        3: {"X": 1, "x": 2, ".": 5},
        4: {"X": 1, "x": 2, ".": 5},
        5: {".": 5, "x": 5, "X": 5},
    }
    # split the phrase in words
    l = t.split()
    li = []
    s = " "
    # apply the word breaker
    for i in range(len(l)):
        li.append(word_breaker(dfa, 0, {1, 2, 3, 4}, l[i]))
        s = " ".join(li)
    return s
