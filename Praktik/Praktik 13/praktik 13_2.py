class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        if self == '':
            return False
        return (s * (len(self) // len(s))) == self

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]



s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True