import responder

api = responder.API()


@api.route("/")
def welcome(req, resp):
    resp.text('hello world')


if __name__ == "__main__":
    api.run(port=5555)
