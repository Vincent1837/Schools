import unittest
from lexer import lexer

class TestMiniLispLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = lexer

    def test_numbers(self):
        self.lexer.input("123 -456")
        tokens = [tok for tok in self.lexer]
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, 'NUMBER')
        self.assertEqual(tokens[0].value, 123)
        self.assertEqual(tokens[1].type, 'NUMBER')
        self.assertEqual(tokens[1].value, -456)

    def test_booleans(self):
        self.lexer.input("#t #f")
        tokens = [tok for tok in self.lexer]
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, 'TRUE')
        self.assertEqual(tokens[1].type, 'FALSE')

    def test_operators(self):
        self.lexer.input("(+ - * / mod > < =)")
        tokens = [tok for tok in self.lexer]
        token_types = [tok.type for tok in tokens]
        self.assertEqual(token_types, [
            'LPAREN', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MOD',
            'GREATER', 'SMALLER', 'EQUAL', 'RPAREN'
        ])

    def test_define_statement(self):
        self.lexer.input("(define x 5)")
        tokens = [tok for tok in self.lexer]
        token_types = [tok.type for tok in tokens]
        self.assertEqual(token_types, ['LPAREN', 'DEFINE', 'ID', 'NUMBER', 'RPAREN'])

    def test_illegal_character(self):
        self.lexer.input("@")
        with self.assertLogs() as log:
            tokens = [tok for tok in self.lexer]
        self.assertIn("Illegal character", log.output[0])

if __name__ == '__main__':
    unittest.main()
