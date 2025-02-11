__import__("os").system("pip install llama-cpp-python --target=. -qq")

import urllib.request
from llama_cpp import Llama

MODEL_URL = "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf"
MODEL_DIR = "models"
MODEL_PATH = f"{MODEL_DIR}/llama-2-7b.Q4_K_M.gguf"

if not __import__("os").path.exists(MODEL_DIR):
    __import__("os").mkdir(MODEL_DIR)

if not __import__("os").path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model downloaded!")

print("Loading model...")
llm = Llama(model_path=MODEL_PATH)

print("Running test prompt...")
output = llm("Hello, how are you?")
print("\nAI Response:\n", output["choices"][0]["text"])
