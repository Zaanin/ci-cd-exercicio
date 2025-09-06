from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(status="ok", message="faaaala galera beleza beleza")

if __name__ == "__main__":
    # Porta 8000 para facilitar testes locais e no runner
    app.run(host="0.0.0.0", port=8000)
