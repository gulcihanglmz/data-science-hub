from fasthtml.common import *

app = FastHTML()

show_message = True

@app.route("/")
def index():
    if show_message:
        return Div(P("This message is visible."))
    else:
        return Div(P("No message to display."))

serve()
