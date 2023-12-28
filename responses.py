def handle_response(message):
    p_message = message.lower()

    if "scp" in p_message:
        l_message = p_message.split()
        return "https://scp-wiki.wikidot.com/scp-" + l_message[1]
