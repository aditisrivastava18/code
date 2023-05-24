import os

class Agent:
    def __init__(self):
        self.file_contents = []

    def upload_files(self, files):
        for file in files:
            if os.path.isfile(file):
                with open(file, 'r') as f:
                    self.file_contents.append(f.read())

    def answer_question(self, question):
        for content in self.file_contents:
            if question in content:
                return self.extract_answer(content)
        return self.generate_default_answer()

    def extract_answer(self, content):
        # Implement your logic to extract the answer from the content
        # This could involve text processing, machine learning, or any other method suitable for your specific use case
        return "Answer extracted from the file"

    def generate_default_answer(self):
        # Implement your logic to generate a default answer
        # This could be a fallback answer or any other response when the question is not found in the uploaded files
        return "Default answer"

# Example usage
agent = Agent()

# User uploads files
files = ['file1.txt', 'file2.txt']
agent.upload_files(files)

# User asks a question
question = input("Ask a question: ")

# Agent answers the question
answer = agent.answer_question(question)
print(answer)

