from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Html(
        Body(
            Button("Open Modal", hx_get="/modal"),
            Div(id="modal-content")
        )
    )

@app.route("/modal")
def modal():
    return Div("This is a modal dialog.", style="background-color:white; border:1px solid black;")

serve()

