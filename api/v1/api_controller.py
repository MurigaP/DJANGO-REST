__author__ = 'hudutech'

from inventory.models import consumers

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from inventory.models import consumers

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
            api_response['message'] = "Error occurred [Error info -->> {}".format(str(e))
            return HttpResponse(json.dumps(api_response), content_type='application/json')

    elif request.method == 'PUT':
        data = json.loads(request.body)

        try:
            # since account no is the pk we use it to update other fields
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

            consumer = get_object_or_404(consumers, accountno=account_no)
            consumer.custname = consumer_name
            consumer.zoneid = zone_id
            consumer.zonename = zone_name
            consumer.Route = route_id
            consumer.routename = route_name
            consumer.plotnumber = plot_number
            consumer.balance = balance
            consumer.serialno = serial_no
            consumer.phone = phone_number
            consumer.connectioncode = connection_code
            consumer.connectionstatus = connection_status

            api_response['statusCode'] = 201
            api_response['message'] = "Consumer Updated Successfully"
            return HttpResponse(json.dumps(api_response), content_type='application/json')
        except (IntegrityError, KeyError) as e:
            api_response['statusCode'] = 500
            api_response['message'] = "Error occurred [Error info -->> {}".format(str(e))
            return HttpResponse(json.dumps(api_response), content_type='application/json')

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        try:
            account_no = data['account_no']

            consumer = get_object_or_404(consumers, accountno=account_no)
            consumer.delete()

            api_response['statusCode'] = 204
            api_response['message'] = "Consumer deleted Successfully"
            return HttpResponse(json.dumps(api_response), content_type='application/json')

        except KeyError, e:

            api_response['statusCode'] = 500
            api_response['message'] = "Error occurred [Error info -->> {}".format(str(e))
            return HttpResponse(json.dumps(api_response), content_type='application/json')

    elif request.method == 'GET':
        consumer_object = consumers.objects.all()

        consumers_list = []

        for consumer in consumer_object:
            response = dict({})

            response['connection_code'] = consumer['connection_code']
            response['consumer_name'] = consumer['consumer_name']
            response['zone_id'] = consumer['zone_id']
            response['zone_name'] = consumer['zone_name']
            response['route_id'] = consumer['route_id']
            response['route_name'] = consumer['route_name']
            response['plot_number'] = consumer['plot_number']
            response['balance'] = consumer['balance']
            response['serial_no'] = consumer['serial_no']
            response['phone_number'] = consumer['phone_number']
            response['connection_status'] = consumer['connection_status']

            consumers_list.append(response)
        return HttpResponse(json.dumps(consumers_list), content_type='application/json')

    else:
        api_response['statusCode'] = 500
        api_response['message'] = "INVALID HTTP REQUEST METHOD ONLY POST, DELETE, PUT, GET ALLOWED"
    return HttpResponse(json.dumps(api_response), content_type='application/json')











