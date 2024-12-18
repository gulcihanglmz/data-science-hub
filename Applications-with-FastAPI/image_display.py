from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Div(
        Img(src="https://miro.medium.com/v2/resize:fit:972/1*2s2da7ppFtbnqJxzhkc68w.jpeg"),
        P("This is an image.")
    )

serve()