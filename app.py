from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="auto"
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ]
)

print(completion.choices[0].message)