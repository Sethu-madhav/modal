import modal
import subprocess

image = modal.Image.debian_slim().uv_pip_install("torch")
app = modal.App(name="test-app", image=image)


@app.function(gpu="A10")
def test(name: str):
    print(f"hello {name}")
    print("Running nvidia-smi...")
    output = subprocess.run(["nvidia-smi"], capture_output=True, text=True, check=True)
    print(f"{output.stdout}")


@app.local_entrypoint()
def main():
    test.remote("arjun")
