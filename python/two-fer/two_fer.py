def two_fer(*name):
    if len(name) == 0:
        return "One for you, one for me."
    return "One for {}, one for me.".format(name[0])