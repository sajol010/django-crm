from rest_framework.response import Response

def success(data, statusCode=200, msg=None):
    response  = {
        'success': True,
        'data': data
    }
    if msg is not None:
      response['msg'] = msg

    return Response(response, statusCode)


def error(msg, errors=None, statusCode=400):
    response  = {
        'success': False,
        'msg': msg
    }
    if errors is not None:
      response['errors'] = errors

    return Response(response, statusCode)
