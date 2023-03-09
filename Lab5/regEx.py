import re

def test1():
    text = input()
    pattern = "ab*"
    m = re.findall(pattern, text)
    print(m)

def test2():
    text = input()
    pattern = "ab{2,3}"
    m = re.findall(pattern, text)
    print(m)

def test3():
    text = input()
    m = re.split("_", text)
    result = []
    for i in range(len(m) - 1):
        if m[i] != ' ' and m[i + 1] != ' ' and m[i].islower() and m[i + 1 ].islower():
            result.append(f"{m[i]}_{m[i+1]}")
    print(result)

def test4():
    text = input()
    pattern = "[A-Z][a-z]+"
    m = re.findall(pattern, text)
    print(m)

def test5():
    text = input()
    pattern = "a.+b$"
    m = re.findall(pattern, text)
    print(m)

def test6():
    text = input()
    m = re.sub("[,. ]", ":", text)
    print(m)

def test7():
    text = input()
    split=re.split("_",text)
    print(split[0]+"".join(x.title() for x in split[1::]))

def test8():
    text = input()
    print(re.findall("[A-Z][^A-Z]*", text))

def test9():
    text = input()
    m = re.findall("[A-Z][a-z]*", text)
    print(' '.join(m))

def test10():
    text = input()
    print('_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
        re.sub('([A-Z]+)', r' \1',
        text.replace('-', ' '))).split()).lower())