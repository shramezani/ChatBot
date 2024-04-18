import gradio as gr
import requests


def send_message_to_chatbot(message, history):
    response = requests.post(
        "http://0.0.0.0:8080/chat/",
        json={"message": message, "history": history}
    )
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return (
            "Error from chatbot API:  "
            f"Status:{str(response.status_code)} {response.text}"
        )


interface = gr.ChatInterface(
    fn=send_message_to_chatbot,
    title="Simple Chatbot with FastAPI and Gradio",
    description="Type a message and get a response from a GPT-2 based chatbot.",
)
if __name__ == "__main__":
    interface.launch(share=False)
