import os
import openai
import gradio as gr

# API as a string (Is to be removed)
openai.api_key = "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"

# Says it the text is from AI or Human
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

# Input box prompt
prompt = "Hey! I'm an AI. How can I help? "


# CREATE FUNCTION FOR RESPONSE
# Function takes one argument that is "prompt"
def openai_create(prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    # Taking the response and returning the text
    return response.choices[0].text


# FUNCTION TAKING ARGUMENTS (input, history)
# Function is required for gradio application to work (arguments wrapped inside a function)
# input = takes text
# history = stores the state in the app to keep the knowledge of the context of the memory
def chatgpt_app(input, history):
    history = history or []   # Empty at first
    s = list(sum(history, ()))
    s.append(input)  # Send the current message to the openAI + as a whole
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))  # Response gets added as output
    return history, history  # History gets added one input, one output


# INTERFACE STARTs
# Display of chatGPT like Blocks
block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Text-To-Text Python Gradio App with OpenAI API</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_app, inputs=[
                 message, state], outputs=[chatbot, state])

block.launch(debug=True)
