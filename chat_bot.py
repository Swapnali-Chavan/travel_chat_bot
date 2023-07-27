import openai
import os

openai.api_key  = 'Enter your key'

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

messages =  [  
{'role':'system', 'content':'You are an travel assistant who guides user regarding to which destination he can travel,\
  travel tips, budget, best time to visit.'},    
{'role':'user', 'content':'Why do we travel , tell me in 10 words?'},   
{'role':'assistant', 'content':'Exploration, adventure, relaxation, culture, learning, relationships, growth, escape, celebration, diversity.'},   
{'role':'user', 'content':'when should we travel?'},
{'role':'assistant', 'content':'The best time to travel depends on various factors, including:\
Destination: Consider the climate and weather conditions of your chosen destination.\
Season: Different places may have peak seasons or off-peak seasons for tourists.\
Purpose: Decide whether you want to experience specific events, festivals, or activities.\
Budget: Plan your travel according to your budget and availability.\
Safety: Be aware of any travel advisories or restrictions for your destination'},    
]
print("Hi I am Travel bot. How may I help you ?")
temperature = 0
while True:
    question = input("Ask me anything about travel:  (Type Bye to exit)")
    if question == "Bye":
        print("-----Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!------")
        break
    messages.append({'role': 'user', 'content':question})
    response = get_completion_from_messages(messages, temperature=0)
    messages.append({'role':'assistant', 'content':response})
    print(response)

