def statement_generator(text, decoration):


    ends = decoration * 5


    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return""


statement_generator("look - stars","*")