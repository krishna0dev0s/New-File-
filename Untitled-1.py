import openai
openai.api_key ="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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{"role": "user","content": prompt}]
    )
   
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("krishna: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("krishna: ", response)
