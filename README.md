# Assignment - Language Consistency for Chatbot 

## Objective
Ensure that the chatbot replies in the same language as the user's conversation language (Hindi, English, or Hinglish).

## What I Did
- Modified the `base_prompt` by adding a clear instruction:
  > "Important Note: Always detect the customer's language and respond in the same language. If user types in Hindi, respond in Hindi; if user types in English, respond in English; if user types in Hinglish (Hindi using English letters), respond in Hinglish."
- Did not modify `content`, `conversation`, or `completion_prompt`.
- Used the OpenAI `gpt-4o` model to test the modified data.

## Files Included
- `updated.json` — Updated JSON file with corrected prompts.
- `wow_code.py` — Streamlit visualization script to test responses.
- `README.md` — This documentation file.

## Testing Result
- Verified that Hindi conversations get Hindi replies.
- Verified that English conversations get English replies.
- Language switching handled correctly.
- Response time was fast and quality of answers remained good.

## Notes
- OpenAI API Key kept private during actual submission.
- Minor HumanMessage/AIMessage format appeared but response content was valid.
