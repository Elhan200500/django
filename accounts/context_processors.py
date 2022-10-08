from datetime import datetime


def get_time(request):
    current_datetime = datetime.now()
    return {'time': current_datetime}


