
from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Html(
        Body(
            Form(Input(type="file", name="file"), Button("Upload", hx_post="/upload")),
            Div(id="response")
        )
    )

@app.route("/upload", methods=["POST"])
def upload(file):
    # Process file here (not implemented)
    return Div(f"Uploaded file name is {file.filename}")

serve()

