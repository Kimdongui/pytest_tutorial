from execute_print import get_greeting_string

def hey_ho_check():
    assert isinstance(get_greeting_string("CLUE"), str)

class CheckGreeting:
    """
        This class check greeting method
    """

    def greeting_check(self):
        assert isinstance(get_greeting_string("CLUE"), str), "It's not string type"
        assert "Hello" in get_greeting_string("CLUE"), "There is no say hello in greeting msg"
