LONG_ANSWER = {
    "text" : """
Answer the following question with correct answer. Letter and a very brief explanation of why you exluded other options.
Note that the text is extract using OCR and might contain artifacts.

extracted_text: {extracted_text}
answer:
""",
    "input_variables" : ['extracted_text']
}

SHORT_ANSWER = {
    "text" : """
Answer the following question with correct answer with correct options only. Do not add any extra text.
Note that the text is extract using OCR and might contain artifacts.

extracted_text: {extracted_text}
answer:
""",
    "input_variables" : ['extracted_text']
}

LETTER_ANSWER = {
    "text" : """
Answer the following question with correct answer with ONLY the correct letter options only. Do not add any extra text.
Note that the text is extract using OCR and might contain artifacts.

extracted_text: {extracted_text}
correct_option_letter:
""",
    "input_variables" : ['extracted_text']
}