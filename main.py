import flask as fl, json, re, sys
import preproc

app = fl.Flask(__name__, static_folder = None)
html = preproc.HTMLpreproc(live_reload = True, flask_features = True)


with open(f"{app.root_path}/discord_data/{sys.argv[1]}/scrape.json", "r") as f:
    scrape = json.load(f)

with open(f"{app.root_path}/discord_data/{sys.argv[1]}/info.json", "r") as f:
    info: dict = json.load(f)


def links(text: str):
    return re.sub(r"(https?://[^\s]+)", lambda m: f"<a href=\"{m.group(0)}\">{m.group(0)}</a>", text)

def mentions(text: str):
    return re.sub(r"(@\w+)", lambda m: f"<span class=\"mention\">{m.group(0)}</span>", text)


@app.route("/resources/<path:path>")
def resources(path):
    match path:
        case "style.css":
            return fl.send_from_directory(f"{app.root_path}/static/css", "style.css", mimetype = "text/css")
        
        case "modal.js":
            return fl.send_from_directory(f"{app.root_path}/static/js", "modal.js", mimetype = "text/javascript")
        
        case "visible.js":
            return fl.send_from_directory(f"{app.root_path}/static/js", "visible.js", mimetype = "text/javascript")
        
        case _:
            print(path)
            return "404", 404
        
@app.route("/")
def index():
    messages = []

    a = fl.request.args.get("a")

    if a: min_, max_ = list(map(int, a.split(":")))
    else: min_, max_ = 0, 100

    for i, message in enumerate(scrape[min_:max_][::-1]):
        files = {}

        if message["attachments"]:
            for i, url in enumerate(message["attachments"]):
                filename = f"{message["message_id"]}.{i}.{url.split("?", 1)[0].rsplit(".", 1)[1]}"
                
                files[f"/files/{filename}"] = filename

        reactions = {}

        if message["reactions"]:
            for reaction in message["reactions"]:
                reactions[reaction["name"]] = reaction["count"]

        content = message["content"]

        for func in [links, mentions]:
            content = func(content)

        if not message["attachments"] and not message["content"]:
            content = "<span class=\"call\"><b>📞 Call started 📞</b></span>"

        messages.append(
            html.fl_render(
                "_message",
                avatar_img = info["avatars"].get(message["author_username"], info["avatar_default"]),
                username = message["author_username"],
                timestamp = message["timestamp"],
                content = content,
                images = files,
                footer = message["message_id"],
                reactions = reactions
            )
        )

    return html.fl_render("index", messages = messages)

@app.route("/files/<path:path>")
def file_(path):
    return fl.send_from_directory(f"{app.root_path}/discord_data/{sys.argv[1]}/files", path)

if __name__ == "__main__":
    app.run(port = 80)