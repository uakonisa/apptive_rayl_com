{
    "name": "Manon : Backend Theme",
    "summary": "Manon: A clean elegant user interface designed for Odoo administrative  interface.",
    "category": "Theme/Backend",
    "version": "1.0.4",
    "sequence": 1,
    "author": "Webkul Software Pvt. Ltd.",
    "website": "http://www.webkul.com",
    "description": "https://store.webkul.com/Manon-Backend-Theme.html",
    # "live_test_url"        :  "http://odoodemo.webkul.com/?module=backend_theme_manon",
    "depends": [
        'base',
        'web',
        'mail',
        'web_editor',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/fonts.xml',
        'data/colors.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    "qweb": [
        'static/src/xml/themeslider.xml',
        'static/src/xml/menu.xml',
    ],
    "images": [
        'static/description/Banner.png',
        'static/description/manon_screenshot.png',
    ],
    "application": False,
    "installable": True,
    # "price"                :  99,
    # "currency"             :  "EUR" ,
    # "pre_init_hook"        :  "pre_init_check",

}
