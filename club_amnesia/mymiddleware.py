class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #This code is executed before the next middleware is called
        request.META['CUSTOM_KEY'] = 'Joshua was here'
        response = self.get_response(request)
        #This code is called after the view is called i.e on the return journey
        assert False
        return response