from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr
# initialize the models
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="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"
)

def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return openai.invoke(formated_prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)