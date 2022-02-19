def response(hey_bob : str):
    hey_bob = hey_bob.strip()
    return ('Sure.', "Calm down, I know what I'm doing!")[hey_bob.isupper()] \
        if hey_bob.endswith('?') else 'Whoa, chill out!' \
        if hey_bob.isupper() else 'Whatever.' \
        if hey_bob else 'Fine. Be that way!'