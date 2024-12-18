from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Div(P("Styled Text"), style="color:red; font-weight:bold;")

serve()
