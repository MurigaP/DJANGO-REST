__author__ = 'hudutech'

from inventory.models import consumers

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError

import json

api_response = dict({})

@csrf_exempt
@require_http_methods(['POST,PUT,DELETE, GET'])
def consumer_endpoint(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            account_no = data['account_no']
            connection_code = data['connection_code']
            consumer_name = data['consumer_name']
            zone_id = data['zone_id']
            zone_name = data['zone_name']
            route_id = data['route_id']
            route_name = data['route_name']
            plot_number = data['plot_number']
            balance = data['balance']
            serial_no = data['serial_no']
            phone_number = data['phone_number']
            connection_status = data['connection_status']

            consumer = consumers.objects.create(
                accountno=account_no,
                connectioncode=connection_code,
                custname=consumer_name,
                zoneid=zone_id,
                Route=route_id,
                zonename=zone_name,
                routename=route_name,
                plotnumber=plot_number,
                balance=balance,
                serialno=serial_no,
                phone=phone_number,
                connectionstatus=connection_status
            )
            consumer.save()

            api_response['statusCode'] = 200
            api_response['message'] = "Consumer Registered Successfully"
            return HttpResponse(json.dumps(api_response), content_type='application/json')

        except (IntegrityError, KeyError) as e:
            api_response['statusCode'] = 500
            api_response['message'] = "Error occurred [Error info->> {}".format(str(e))
            return HttpResponse(json.dumps(api_response), content_type='application/json')




