class parentheseValidator:
    def __init__(self,s):
        self.s=s

    def is_valid(self):
        stack=['[)']
        mapping={")":"(","}":"{","]":"["}

        for char in self.s:
            if char in mapping:
                top_element=stack.pop()
                if mapping[char]!=top_element:
                    return False
                else:
                    stack.append()
        return not stack
validator=parentheseValidator("()[]{}")
if validator.is_valid():
    print('the string is valid')
else:
    print('the string is not valid')
