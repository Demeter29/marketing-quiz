import json
import re

def parse_questions(text):
    
    blocks = []
    lines = text.split('\n')

    block = []

    open = True
    for line in lines:
        
        if is_question(line):
            open = True
            block = []
            block.append(line)
        elif is_answer(line):
            block.append(line)
        elif is_solve(line):
            if(len(block) > 2):        
                index = [ord(line[line.find(':') + 2].lower()) - 96]
                block.append(index)
                blocks.append(block)

            block = []
            open = False
        else:
            if open and len(block) == 1:
                block[0] += line
    
    
    return blocks

def is_question(s):
    # Define a regular expression pattern to match numbers followed by a closing parenthesis
    pattern = r'^\d+\)'
    # Use re.match to check if the string starts with the pattern
    return bool(re.match(pattern, s))

def is_answer(s):
    # Define a regular expression pattern to match numbers followed by a closing parenthesis
    pattern = r'[A-Z]\)'
    # Use re.match to check if the string starts with the pattern
    return bool(re.match(pattern, s))

def is_solve(s):
    # Check if the string starts with "answer:" (case-insensitive)
    return s.startswith("Answer:")


# File paths
input_file_path = 'bank.txt'
output_file_path = 'data.js'

# Read the input text from a file
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Parse the questions
parsed_questions = parse_questions(text)

# Convert the parsed questions to JSON
json_output = json.dumps(parsed_questions, indent=4, ensure_ascii=False)

# Write the JSON output to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(json_output)

print(f"JSON output has been written to {output_file_path}")
