from openai import OpenAI


# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general task like Alexa and Google Cloud."},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)