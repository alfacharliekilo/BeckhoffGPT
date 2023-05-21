import openai

openai.api_key = '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'

query = input("Provide a string to translate into French: "
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response.choices[0].text.strip())