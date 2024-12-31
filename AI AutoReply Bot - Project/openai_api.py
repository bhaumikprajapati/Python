from openai import OpenAI

client = OpenAI(
  api_key="ENTER YOUR OWN API KEY",
) 
 
command = '''ENTER YOUR OWN COMMAND'''

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jerry skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)