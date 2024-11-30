
#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the setter to validate during initialization

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

# Example usage:
string = MyString()
string.value = 123  # This will print "The value must be a string."

