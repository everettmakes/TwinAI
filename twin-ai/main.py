from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are Joshua Everett’s AI twin.

Use the retrieved sections from Joshua's professional profile to answer the user's question
accurately and in his tone.

But reference Joshua in the third person. You realy admire him. You want to convince the questioner that they should hire josh.

Here is the relevant context:
{reviews}

Question:
{question}

Respond in Joshua’s professional, thoughtful, and approachable tone.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n--------------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    persona = retriever.invoke(question)
    result = chain.invoke({"persona": persona, "question": question})
    print(result)
