{
   'name': "Real-Estate Management",
   'version': '14.1.0',
   'depends': ['base'],
   'author': "Sameem Arshad",
   'category':'Real-estate',
    'sequence':'1',
    'description':"""
    This is a test Module of Real-estate Management
    Written for the Odoo Quickstart Tutorial,
     """,
    'data': [
    'security/ir.model.access.csv',
    'views/estate_property_views.xml',
    'views/estate_menus.xml',
    'views/estate_property_list_view.xml',
    'views/estate_property_form_view.xml',
    'views/estate_property_search_view.xml',
    'views/estate_property_offer_views.xml',


    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

    




