def testing(tests, func):
    print(f"testing {func.__name__}...")
    for key in tests:
        result = func(key)
        B = result == tests[key]
        if not (B):
            print(key)
            return B
    return True


# Solutions


def bp_0(ch):
    stack = []
    for letter in ch:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop(-1)
    return len(stack) == 0


def bp_1(ch):
    n = 0
    idx = 0
    while (idx < len(ch)) and (n >= 0):
        letter = ch[idx]
        if letter == "(":
            n += 1
        elif letter == ")":
            n -= 1
        idx += 1
    return n == 0


def bp_2(ch, n=0):
    if n < 0:
        return False
    elif ch == "":
        return n == 0
    else:
        letter = ch[0]
        if letter == "(":
            return bp_2(ch[1:], n + 1)
        elif letter == ")":
            return bp_2(ch[1:], n - 1)
        else:
            return bp_2(ch[1:], n)


def bp_3(ch):

    while len(ch) != 0:
        idx_end = ch.find(")")
        if idx_end == -1:
            return ch.find("(") == -1
        else:
            idx_start = ch[:idx_end].rfind("(")
            if idx_start == -1:
                return False
            else:
                ch = ch[:idx_start] + ch[idx_end + 1 :]
    return True


def bp_4(ch):

    idx_end = ch.find(")")
    if idx_end == -1:
        return ch.find("(") == -1
    else:
        idx_start = ch[:idx_end].rfind("(")
        if idx_start == -1:
            return False
        else:
            return bp_4(ch[:idx_start] + ch[idx_end + 1 :])


def bp_5(ch):
    if ch == "":
        return True
    else:
        letter = ch[0]
        if letter == ")":
            return False
        elif letter == "(":
            idx = ch.find(")")
            if idx == -1:
                return False
            else:
                return bp_5(ch[1:idx]) and bp_5(ch[idx + 1 :])
        else:
            return bp_5(ch[1:])


if __name__ == "__main__":

    tests = {
        "John": True,
        "()": True,
        "(": False,
        ")(": False,
        "(())": True,
        "((((()))))": True,
        "(ok)": True,
        "())(": False,
        "(()(()))()((((()))))": True,
    }

    solutions = [bp_0, bp_1, bp_2, bp_3, bp_4, bp_5]

    for solution in solutions:
        testing(tests, solution)
        print("--------")
