# App 1: Text-To-Text Generative AI App using Gradio, OpenAI API

## Prerequisite

<details>
<summary>Install (Python/PIP)</summary>
  
- [Install Python3](https://python.org/)
- [OpenAI DALLE•2 API KEY](https://beta.openai.com/)
  > We add the key later
</details>

---

## Step 1: Folder + Files

<details>
<summary>Create Folder Structure</summary>

- Create a new folder `1-text-to-text`
  > This is our first gradio app.
- Change directory `cd 1-text-to-text `
- Create a new file `app.py` inside the folder
  > Main file
- Create a new file `requirements.txt`. Inside the file add:

```bash
gradio
openai
```

> These are the libraries that needs to be installed.

</details>

---

## Step 2: Python Library Installation

<details>
<summary>Install Gradio, OpenAI libraries</summary>
  
> NOTE: If ```pip``` or ```python``` command does not work please use ```pip3``` or ```python3``` respectively. 
  
- Install Python OpenAI Module (using pip)
```bash
  pip install gradio
```
- Install Python customtkinter Module (using pip)
```bash
  pip install openai
```
- Incase any other modules are missing locally, use:
```bash
  pip install <MODULE_NAME> 
```
> NOTE: To verify if the libraries are installed or not run command: ```pip list```
</details>

---

## Step 3: Import Libraries + API Key

<details>
<summary>Import gradio, openai and connect to the API</summary>

- Open the `app.py` file and add:

```bash
  import os
  import openai
  import gradio as gr

  openai.api_key = "xxxxxx"
```

> Make sure when you create a new secret key you copy it otherwise you cannot get.
> Create, Copy & Replace the API Key from OpenAI website under 'User the Setting > View API Keys'.

</details>

---

## Step 4: Add app.py Function

<details>
<summary>Adding Functions under app.py file</summary>

- Open the `app.py` file and add:

```bash
# Says it the text is from AI or Human
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

# Input box prompt
prompt = "Hey! I'm an AI. How can I help? "
```

```bash
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
```

```bash
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
```

```bash
#INTERFACE STARTs
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
```

</details>

---

## Step 5: Deploy the App

<details>
<summary>Deploying the Gradio App</summary>

### To Run The App

- From the root directory of 'app.py', run in terminal"

```bash
  python app.py
```

or

```bash
  python3 app.py
```

### To Deploy The App

- From the root directory of 'app.py', run in terminal"

</details>

---
