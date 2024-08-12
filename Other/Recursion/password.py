def verify(password):
    trial = input()
    while trial != password:
        trial = verify(password)
    return trial


if __name__ == "__main__":
    password = "123456"
    print(verify(password))
