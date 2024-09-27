def all_variants(text):
    for length in range(1, len(text) + 1):
        for run in range(len(text) - length + 1):
            yield text[run:run + length]


a = all_variants("abc")
for i in a:
    print(i)
