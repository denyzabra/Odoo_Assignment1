{
    'name': 'Purchase Request',
    'version': '1.0',
    'summary': 'Module for managing purchase requests',
    'description': 'This module allows employees to send purchase requests to the Procurement department',
    'author': 'abraham',
    'category': 'Purchases',
    'depends': ['purchase'],
    'data': [
        'views/purchase_request_views.xml',
    ],
    'installable': True,
    'application': True,
}
