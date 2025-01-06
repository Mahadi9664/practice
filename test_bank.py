from bank import value

def main():
    test_return0()
    test_return20()
    test_return100()
    
    


def test_return0():
    assert value('hello') == '$0'
    assert value('hello man') == '$0'
    assert value('Hello gi') == '$0'

def test_return20():
    assert value('hi') == '$20'
    assert value('hey') == '$20'
    assert value('hola') == '$20'

def test_return100():
    assert value('meow') == '$100'
    assert value('f man') == '$100'

if __name__ == "__main__":
    main()