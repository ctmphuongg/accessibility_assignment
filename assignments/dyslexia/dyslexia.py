import random
import PyPDF2

# Part 1: Read PDF File
def read_pdf(pdf_path):
    # Open the PDF file and returns: text
    # TODO
    pass

# Part 2: Text Formatting

# Function to split text into words and letters
def space_formatter(text):
    # Split the text into words first, then into individual letters
    # TODO
    pass

# Function to format each letter with random styling
def letter_formatter(text):
    # List of formatting options
    formats = ['lowercase', 'uppercase', 'bold', 'italic']
    
    letter_list = space_formatter(text)
    formatted_text = []
    
    # TODO
    pass

# Part 3: Evaluate Readability

def readability_check(formatted_text):
    # Check for readability issue: 5 consecutive letters with the same format and no spaces
    # TODO
    pass

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
