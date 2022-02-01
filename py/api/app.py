import logging

from eve import Eve

from .pre_processing import PreProcessingException, create_order

log = logging.getLogger(__name__)


def boot():
    """Function to establish all middlewares to the flask app"""
    app = Eve()

    @app.errorhandler(PreProcessingException)
    def handle_general(error):
        return {
            "_status": "ERR",
            "_issues": error.issues,
            "_error": {
                "code": 422,
                "message": "Insertion failure: 1 document(s) contain(s) error(s)"
            }
        }, 422

    app.on_insert_orders += create_order

    return app


app = boot()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)