import google.generativeai as palm

palm.configure(api_key="YOUR API KEY GOES IN THIS SECTION")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [
        {"category":"HARM_CATEGORY_DEROGATORY","threshold":1},
        {"category":"HARM_CATEGORY_TOXICITY","threshold":1},
        {"category":"HARM_CATEGORY_VIOLENCE","threshold":2},
        {"category":"HARM_CATEGORY_SEXUAL","threshold":2},
        {"category":"HARM_CATEGORY_MEDICAL","threshold":2},
        {"category":"HARM_CATEGORY_DANGEROUS","threshold":2}
    ],
}

while True:
    user_input = input("Please provide your input or type 'exit' to stop: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    prompt = f"""input: i need you to organize my data into tables please
output: Sure! I can help you with that what type of data
input: many types of data and i need ie to stay organized please
output: As you wish, I just need to know what data you desire processed,
input: {user_input}
output:"""

    response = palm.generate_text(
        **defaults,
        prompt=prompt
    )
    
    print(response.result)
    continue_response = input("Do you want to continue? (yes/no): ")
    
    if continue_response.lower() != 'yes':
        print("Exiting the program.")
        break
