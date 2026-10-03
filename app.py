import time
from huggingface_hub import InferenceClient

client = InferenceClient(provider="auto")

MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"

topic = input("Enter a topic: ").strip()

if not topic:
    print("Please enter a topic.")
    exit()

prompt = f"""
Create exactly 5 study flashcards about {topic}.

For each flashcard:
1. Write a question.
2. Write a short answer.

Use this format:

Flashcard 1
Question: ...
Answer: ...

Flashcard 2
Question: ...
Answer: ...

Flashcard 3
Question: ...
Answer: ...

Flashcard 4
Question: ...
Answer: ...

Flashcard 5
Question: ...
Answer: ...

Keep the answers suitable for a 2nd-year
computer science student.
"""

try:
    start = time.time()

    result = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    latency = time.time() - start

    print("\nGenerated Flashcards:\n")
    print(result.choices[0].message.content)
    print(f"\nModel: {MODEL_ID}")
    print(f"Response time: {latency:.2f} seconds")

except Exception as e:
    print("\nError:", e)
    print("Check your Hugging Face login and model availability.")
