

class StringReversal:
    @staticmethod
    def reverse_string_1(s: str) -> str:
        """
        Reverse a string using slicing
        """
        return s[::-1]

    @staticmethod
    def reverse_string_2(s: str) -> str:
        """
        Reverse a string using recursion
        """
        if len(s) == 0:
            return s
        else:
            return StringReversal.reverse_string_2(s[1:]) + s[0]