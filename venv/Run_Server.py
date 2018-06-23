# Run this first to start the server

import os
from api.Microblog import app

if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] = 'Database.db'
    app.secret_key = "password"
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)