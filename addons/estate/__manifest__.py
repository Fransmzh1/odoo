{
    'name': 'Frans Real Estate',
    'version': '1.0',
    'author': 'Frans Diary',
    'sequence': -100,
    'depends': [
        'base'
    ],
    'data' : [
        'security/ir.model.access.csv',
        'models/estate.property.type.csv',
        'views/estate_property_view.xml',
        'views/estate_property_action.xml',
        'views/estate_menus.xml'
    ],
    'application': True,
}