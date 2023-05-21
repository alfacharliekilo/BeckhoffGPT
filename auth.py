import openai

openai.api_key = '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'

query = input("Provide a string to translate into French: "
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response.choices[0].text.strip())