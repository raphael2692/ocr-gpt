LONG_ANSWER = {
    "text" : """
Answer the following question with correct choice or the set of correct choices. 
Also, for every wrong choice, write why it is wrong. 

For example:

Correct choice: 

A - JSON Response

Wrong choices:

B -SOAP: SOAP protocol is not supported
C - XML: XML is not supported
D - XHTML: XHTML is supported only for legacy system, which were not mentioned

Note that the text is extract using OCR and might contain artifacts.
{extracted_text} 
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
Answer to user_prompt using the context given by the user screen content in extracted_text (note that ocr is used and might contain artifacts).

extracted_text: {extracted_text}
correct_option_letter:
""",
    "input_variables" : ['extracted_text']
}

OCR_PROMPT = {
    "text" : """
Act as a coding assistant.
You are given the text extracted from the screen of the user in form of OCR extracted text (extracted_text). 
IMPORTANT: You must answer to user_prompt with valid python code only. Do not add any extra word or character that can break the code you generate.

extracted_text: {extracted_text}
user_prompt: {user_prompt}
generated_code:
""",
    "input_variables" : ['extracted_text', 'user_prompt']
}