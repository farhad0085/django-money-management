from rest_framework.views import APIView
import logging

info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')


class LoggerAPIView(APIView):

    def info(self, message):
        print(message)
        info_logger.info(message)

    def error(self, message):
        print(message)
        error_logger.error(message, exc_info=True)
