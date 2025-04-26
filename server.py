from flask import Flask, request, send_file
import os
import subprocess

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_glb():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400
    file = request.files['file']
    input_path = "In-SC-glTF/input.glb"
    output_path = "Out-glTF/output.glb"
    os.makedirs("In-SC-glTF", exist_ok=True)
    os.makedirs("Out-glTF", exist_ok=True)
    file.save(input_path)

    # Exécuter Supercell-Flat-Converter
     
    subprocess.run(["python", "Supercell-Flat-Converter/main.py", "decode"])

    if os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    return {"error": "Conversion failed"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
