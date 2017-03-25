from __future__ import unicode_literals

from django.db import models


class consumers(models.Model):
    Activated = 'Activated'
    Disconnected = 'Disconnected'

    SEVERITY = (
        (Activated, 'Activated'),
        (Disconnected, 'Disconnected'),

    )
    accountno = models.IntegerField(unique=True)
    connectioncode = models.IntegerField()
    custname = models.CharField(max_length=1000)
    zoneid = models.IntegerField()
    Route = models.IntegerField()
    zonename = models.CharField(max_length=100)
    routename = models.CharField(max_length=100)

    plotnumber = models.CharField(max_length=50)
    balance = models.CharField(max_length=100)
    serialno = models.CharField(max_length=100)
    phone = models.IntegerField()
    connectionstatus = models.CharField(max_length=256, choices=SEVERITY)

    def __unicode__(self):
        return str(self.accountno)


class payments(models.Model):
    paymentid = models.IntegerField(unique=True)
    receiptno = models.IntegerField()
    connectionCode = models.ForeignKey(consumers)
    payment = models.IntegerField()
    paydate = models.DateField()
    paymentmode = models.CharField(max_length=100)

    def __unicode__(self):
        return self.connectionCode

