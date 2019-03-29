from flask import *
import PyLineNotify

# あなたのトークンを入力してください
TOKEN = 'YOURTOCKN'

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Send():
    if request.method == "GET":
        return """
            画像のパスを入力してください。
            <form action="/" method="POST">
            <input name="url"></input>
            </form>"""
    else:
        adr = str(request.form["url"])
        PyLineNotify.send_photo_with_message(token=TOKEN, message=' ', path=adr)
        return """{}を送信しました。画像のパスを入力してください。
            <form action="/" method="POST">
            <input name="url"></input>
            </form>""".format(str(request.form["url"]))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

#debug=True
