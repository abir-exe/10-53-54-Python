letter = '''
    Dear <|Name|>,
    You are Selected!
    <|Date|>
'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24 September, 2050"))
