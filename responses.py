import re


def handle_response(message):
    p_message = message.lower()     # not really necessary, but I'll keep it if I want to add more commands

    l_message = re.split(r"[,\s\-!?:#]+", p_message)
    # print(l_message)   # for debugging
    return "https://scp-wiki.wikidot.com/scp-" + l_message[-1]
