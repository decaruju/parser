from token_type import Token


def lex(text):
    i = 0
    token_chain = []
    while i < len(text):
        chars = text[i]
        for token in Token.__subclasses__():
            if token.match(chars):
                if i + 1 < len(text):
                    next_char = text[i+1]
                    while i + 2 < len(text) and token.match(chars + next_char):
                        chars += next_char
                        i += 1
                        next_char = text[i+1]
                token_chain.append(token(chars, i))
                break
        else:
            raise ValueError(f"Lexer error at `{chars}`, unknown characters")
        i += 1
    return token_chain

