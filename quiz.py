import json

with open('questions.json','r') as file:
    content=file.read()

data=json.loads(content)

for question in data:
    print(question['question_text'])
    for index, option in enumerate(question["Options"]):
        print(f"{index+1}. {option}")
    
    choice=int(input("Enter your answer number: "))
    question["user_answer"]=choice

score=0
for index, question in enumerate(data):
    if question["user_answer"]==question["Answer"]:
        score+=1
        result="Correct Answer"
    else:
        result="Incorrect Answer"
    message=f"Question {index+1}: Your answer: {question['user_answer']}, Correct answer is: {question['Answer']}"
    print(message)

print(f"You got {score} out of {len(data)} questions correct.")