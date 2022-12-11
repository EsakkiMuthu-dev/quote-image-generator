from flask import render_template, send_file, request
from src import Image
from src.config import Config

# this class is resonsible for all routes
class Routes:
    def __init__(self, app) -> None:

        # main route
        @app.route("/")
        def index():
            return render_template("base.html", name="Rasla")

        # route to get image
        @app.route("/download", methods=["POST", "GET"])
        def download():
            if request.method == "POST":
                img = Image.Image().main()
                config = Config()
                return send_file(config.loadimage_path())
