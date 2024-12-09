# Text Formatting for Easier Information Comprehention

## Overview

This project involves analysising and formatting a given text to make it more reading accessible. The objectives include reading a PDF file and converting it into a formattable format, spacing and formatting each letters, and evaluating the readiability of the text.

## Project Objectives

1. **Text Extraction and Preparation**:

   - Import the PDF file using libraries like PyPDF2 in Python.

2. **Text Formatting**:

   - Seperate the words and the letters by space.
   - Randomly format each letters into different formats (lowercase, uppercase, bold, italic).

3. **Readability Analysis**:
   - Check for consistent spacing and formatting.
   - If there is no space between letters and 5 letters in a row have the same formatting, report the program is not working.

## Introduction

Dyslexia is a learning difference that affects how people read and process text, often making traditional formats overwhelming. Challenges like decoding words and maintaining focus can hinder comprehension and retention. 
This project aims to address these challenges by importing a PDF text file, reformatting that text in ways that make it more accessible and easier to read. By extracting and processing text from a source document, you will apply specific formatting techniques—such as adjusting letter spacing, preventing identical formatting for consecutive letters, and ensuring appropriate spaces between words. Additionally, we will evaluate the effectiveness of these changes by checking for the correct formatting.
Additionally, we will evaluate the formatting code by checking for the correct formatting.
This work's aim is to better understand how formatting impacts those with dyslexia and contribute to more inclusive and accessible reading materials.

## Instructions

### Part 1: Read PDF file

1. **Function to Implement**: `read_pdf`
   - Read data from a provided PDF file containing reading material.
   - Convert the text into a plain text format suitable for processing and formatting.

**Guide**:

- Import PyPDF2 to extract text from the PDF file.
- Handle cases where the text is split across lines or pages to ensure seamless content extraction.

### Part 2: Text formatting

1. **Function to Implement**: `space_formatter`
   - Formats text by adjusting spacing between letters and words.
   - Returns formatted text with adjusted spacing.

**Guide**:

- Split the input text into words and letters for detailed formatting.
- Apply spacing rules, ensuring:
    - A space follows each letter if required by the formatting rules.
    - Adequate spacing exists between words for better readability.
 
2. **Function to Implement**: `letter_formatter`
   - Formats letters by randomly changing it to lowercase, uppercase, bold and italic.
   - Returns formatted text with adjusted letter formatting.

**Guide**:

- Use the `space_formatter` function to split the text into letters
- Apply a random formatting style (lowercase, uppercase, bold, or italic) to each letter.
  - Using Python's built in random function randomize the selection of the formatting style

### Part 3: Evaluate Readability

1. **Function to Implement**: `readability_check`
   - Checks whether the formatted text contains 5 consecutive letters with the same formatting and no spaces between them.
   - Returns the formatted text or a message indicating if the program is not working based on the formatting issue.

**Guide**:

- Take 5 consecutive letters and check if they have the same formatting or no space between them.
- If there is no errors output the formatted text.
- If there is an error output a message indicating the program is not working correctly.

**Output**:
  - Formatted text.
   OR
  - An error message.

## Deliverables

1. Python script with the following implemented:
   - `read_pdf` function (Part 1)
   - `space_formatter` and `letter_formatter` functions (Part 2)
   - `readability_check` function (Part 3)
2. A report file (e.g., Markdown or plain text) containing:
   - Description of your approach for each part.

## Resources

- Python libraries: `PyPDF2` (optional).
- Concepts: Text formatting, text splitting, file parsing, randomness.
- Test PDF reading materials provided.

## Evaluation Criteria

1. **Correctness**: Does your code produce the expected results for all test cases?
2. **Code Quality**: Is your code well-organized, commented, and modular?
3. **Report**: Does your report clearly communicate the results and approach?

## Sample PDF
View the link: 
