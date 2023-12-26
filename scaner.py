import re
import json

rouls = {
    'IF_KW': r'if',
    'ELSE_KW': r'else',
    'FOR_KW': r'for',
    'CONST_STR': r'".*?"|\'.*?\'',
    'CONST_NUMBER': r'\d+',
    'PLUS_OP': r'\+',
    'MINUS_OP': r'\-',
    'MULTIPLY_OP': r'\*',
    'DIVIDE_OP': r'\/',
    'LP': r'\(',
    'LCB': r'\{',
    'RP': r'\)',
    'RCB': r'\}',
    'EQUAL_OP': r'==',
    'ASSIGNMENT_OP': r'=',
    'SEMICOLON': r';',
    'IDENTIFIER': r'[a-zA-Z_]\w*'
}





with open('sourcecode.txt', 'r') as f:
    source_code = f.read()




table_token = {}


for key, pattern in rouls.items():
    matches = re.findall(pattern, source_code)
    if matches:
        table_token[key] = matches

print(table_token)

with open('table.json', 'w') as table:
    json.dump(table_token, table, indent=3)
