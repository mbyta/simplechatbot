import gradio as gr
from api_clients.llm_models import get_list_of_all_models
from api_clients.api_clients_helper import get_api_response

def on_user_input_entered(user_input: gr.Textbox, selected_model: gr.Dropdown, chat_history: gr.Chatbot) -> list[str, gr.Chatbot]:
    bot_message = get_api_response(user_input, selected_model)

    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": bot_message})

    return ["", chat_history]

def get_dropdown_options() -> list[str]:
    models_list = get_list_of_all_models()
    models_list.insert(0, "")
    return models_list

def on_model_choice_selected(selected_value: str) -> list[gr.Textbox, gr.Button]:
    is_value_selected = selected_value != ""
    return gr.update(interactive=is_value_selected), gr.update(interactive=is_value_selected)


with gr.Blocks(title="Simple chatbot", fill_width=True) as app:
    with gr.Column():
        gr.Markdown("# Simple chatbot")

        with gr.Row():
            choices_dropdown = gr.Dropdown(choices=get_dropdown_options(), label="Choose a model *", value="", scale=2)
            gr.Column(scale=8)  # to fill the remaining 80% width

        chatbot = gr.Chatbot(height="70vh", type="messages")

        with gr.Row(equal_height=True):
            user_input_textbox = gr.Textbox(show_label=False, placeholder="Enter a prompt here", interactive=False, scale=9)
            send_button = gr.Button("➤", interactive=False, scale=1)

        # event handlers
        choices_dropdown.change(fn=on_model_choice_selected, inputs=choices_dropdown, outputs=[user_input_textbox, send_button])
        user_input_textbox.submit(fn=on_user_input_entered, inputs=[user_input_textbox, choices_dropdown, chatbot], outputs=[user_input_textbox, chatbot])
        send_button.click(fn=on_user_input_entered, inputs=[user_input_textbox, choices_dropdown, chatbot], outputs=[user_input_textbox, chatbot])

if __name__ == "__main__":
    app.launch()