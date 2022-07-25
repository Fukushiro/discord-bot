import cowsay


def make_code_block(message: str) -> str:
    return "```" + message + "```"


def get_ascii_image_for_discord(char_name: str, message: str) -> str:
    return make_code_block(cowsay.get_output_string(char_name=char_name, text=message))
