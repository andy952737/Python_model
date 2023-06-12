# 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
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)