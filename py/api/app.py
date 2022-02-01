import logging
import flask
from eve import Eve


log = logging.getLogger(__name__)


def boot():
    """Function to establish all middlewares to the flask app"""
    app = Eve()

    @app.errorhandler(Exception)
    def handle_general(error):
        raise error

    return app


app = boot()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)