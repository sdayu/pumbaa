
import optparse
import os
from pumbaa import app, get_program_options

if __name__ == '__main__':
    options = get_program_options()
    
    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )
