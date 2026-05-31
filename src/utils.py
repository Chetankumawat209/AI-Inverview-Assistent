
def load_prompt(file_path):
    try:
        with open(file_path,"r") as file:

            return file.read()
    except FileNotFoundError:
        print(f"{file_path} not found ")