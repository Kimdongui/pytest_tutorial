from execute_print import get_greeting_string

def test_hello():
    assert isinstance(get_greeting_string("CLUE"), str), "It's not string type"
    assert "Hello" in get_greeting_string("CLUE"), "There is no say hello in greeting msg"
