import random
import PyPDF2

# Part 1: Read PDF File
def read_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        text = PyPDF2.PdfReader(file)
    return text

# Part 2: Text Formatting

# Function to split text into words and letters
def space_formatter(text):
    # Split the text into words first, then into individual letters
    words = text.split()
    letter_list = [list(word) for word in words]
    return letter_list

# Function to format each letter with random styling
def letter_formatter(text):
    # List of formatting options
    formats = ['lowercase', 'uppercase', 'bold', 'italic']
    
    letter_list = space_formatter(text)
    formatted_text = []
    
    for word in letter_list:
        formatted_word = []
        for letter in word:
            # Randomly choose a format for each letter
            format_style = random.choice(formats)
            
            if format_style == 'lowercase':
                formatted_word.append(letter.lower())
            elif format_style == 'uppercase':
                formatted_word.append(letter.upper())
            elif format_style == 'bold':
                formatted_word.append(f'**{letter}**')
            elif format_style == 'italic':
                formatted_word.append(f'*{letter}*')
        
        formatted_text.append(''.join(formatted_word))
    
    return ' '.join(formatted_text)

# Part 3: Evaluate Readability

def readability_check(formatted_text):
    # Check for readability issue: 5 consecutive letters with the same format and no spaces
    if not any(char == ' ' for char in formatted_text):  # No spaces
        for i in range(len(formatted_text) - 4):
            # Check if there are 5 consecutive letters with the same format
            if formatted_text[i] == formatted_text[i+1] == formatted_text[i+2] == formatted_text[i+3] == formatted_text[i+4]:
                return "Program is not working: 5 consecutive letters have the same format."
    
    return formatted_text

# Example usage:

# Part 1: Read a PDF file
pdf_path = 'test_pdf.pdf'  # Name of PDF file
text = read_pdf(pdf_path)

# Part 2: Format the text with letter formatting
formatted_text = letter_formatter(text)

# Part 3: Check readability
result = readability_check(formatted_text)

# Output the result
print(result)
