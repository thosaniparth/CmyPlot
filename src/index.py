# package imports
from app import app

# local imports
from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK

# initializes all callbacks
import utils.routes
import pages.upload.upload_callbacks
import pages.table.table_callbacks

# initialize services
server = app.server

# site endpoint

if __name__ == '__main__':
    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )