import os
import pytest
from tempfile import mkstemp
from phone_bills.billingcommon.db import BillingDb


@pytest.fixture(scope='module')
def dbo(request):
    db = BillingDb('sqlite:///:memory:')
    db.metadata.create_all()
    if request.param:
        request.param(db)
    return db


@pytest.fixture
def call_start_record():
    return {
        'id': 42,
        'type': 'start',
        'timestamp': '2017-12-12T15:07:13Z',
        'call_id': 71,
        'source': '99988526423',
        'destination': '9993468278'
    }


@pytest.fixture
def call_end_record():
    return {
        'id': 442,
        'type': 'end',
        'timestamp': '2017-12-12T15:14:56Z',
        'call_id': 71
    }
