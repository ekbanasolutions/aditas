class request:

    global headers
    global data
    headers = ''
    data = ''

    def set_headers(self, *args):
        request.headers = args[0]

    def set_data(self, *args, **kwargs):
        request.data = args[0]

