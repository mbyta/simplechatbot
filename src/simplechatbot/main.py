import gradio as gr
from api_clients.llm_models import LlmModels
from api_clients.api_client import ApiClient
import html

class SimpleChatbotApp:
    def __init__(self):
        with gr.Blocks(title="Simple chatbot", fill_width=True) as app:
            with gr.Column():
                gr.Markdown("# Simple chatbot")

                with gr.Row():
                    choices_dropdown = gr.Dropdown(choices=self.get_dropdown_options(), label="Choose a model *", value="", scale=2)
                    gr.Column(scale=8)  # to fill the remaining 80% width

                chatbot = gr.Chatbot(height="70vh", type="messages")

                with gr.Row():
                    user_input_textbox = gr.Textbox(show_label=False, placeholder="Enter a prompt here", interactive=False, scale=9)
                    send_button = gr.Button("➤", interactive=False, scale=1)

                # event handlers
                choices_dropdown.change(fn=self.on_model_choice_selected, inputs=choices_dropdown, outputs=[user_input_textbox, send_button])
                user_input_textbox.submit(fn=self.on_user_input_entered, inputs=[user_input_textbox, choices_dropdown, chatbot], outputs=[user_input_textbox, chatbot])
                send_button.click(fn=self.on_user_input_entered, inputs=[user_input_textbox, choices_dropdown, chatbot], outputs=[user_input_textbox, chatbot])

        self.app = app

    def on_user_input_entered(self, user_input: gr.Textbox, selected_model: gr.Dropdown, chat_history: gr.Chatbot) -> list[str, gr.Chatbot]:
        conversation_context = self.build_conversation_context(chat_history)
        full_input = f"{conversation_context}\n{user_input}" if conversation_context else user_input
        api_client = ApiClient()
        api_response = api_client.get_response(full_input, selected_model)

        chat_history.append({"role": "user", "content": html.escape(user_input)})
        chat_history.append({"role": "assistant", "content": html.escape(api_response)})

        return ["", chat_history]

    def get_dropdown_options(self) -> list[tuple[str, str]]:
        options = [("", "")]
        llm_models = LlmModels()

        for k, v in llm_models.get_all_models().items():
            options.append((v, k )) # (option label, option value)

        return options

    def on_model_choice_selected(self, selected_value: str) -> list[gr.Textbox, gr.Button]:
        is_value_selected = selected_value != ""
        return gr.update(interactive=is_value_selected), gr.update(interactive=is_value_selected)

    def build_conversation_context(self, chat_history: gr.Chatbot):
        conv_context = []
        pair_counter = 0
        conv_counter = 1

        for msg in chat_history:
            content = ""

            if msg["role"] == "user":
                content = f"<query_{conv_counter}>{msg["content"]}</query_{conv_counter}>"
            else:
                content = f"<response_{conv_counter}>{msg["content"]}</response_{conv_counter}>"

            conv_context.append(content)
            pair_counter += 1

            if pair_counter == 2:
                pair_counter = 0
                conv_counter += 1

        result = "\n".join(conv_context)

        return f"<context>{result}</context>" if result else ""

    def launch(self):
        self.app.launch()

if __name__ == "__main__":
    chat_app = SimpleChatbotApp()
    chat_app.launch()