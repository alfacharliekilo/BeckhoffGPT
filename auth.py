import openai


openai.api_key = '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'

user_input = input("Provide a string to translate into French: ")
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{user_input}'",
  max_tokens=60
)

print(response.choices[0].text.strip())