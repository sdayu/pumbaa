import pumbaa

def main():
    options = pumbaa.get_program_options()
    app = pumbaa.create_app()

    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )
