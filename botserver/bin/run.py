import logging
from botserver.log import set_logger_options
from botserver.src.app import Server_API

api_server_logger = logging.getLogger('server_api')
set_logger_options(api_server_logger, 'server_api')

server = Server_API()
server.start(5000)
