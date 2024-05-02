{
    "name": "addons personnaliser ",
    "version": "17.0.0.0",
    "category": "Generic Modules/Others",
    "description": """ créations des addons personnalisés""",
    "author": "Alan FINITI",
    "depends": ["purchase", "hr_attendance", "hr_contract", "mrp", "product", "stock", "website_sale","stock_sms"],
    "data": [
        "security/lamarmitte_security.xml",
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/allergen_category_views.xml",
        "views/product_views.xml",
        "views/vat_views.xml",
        "views/menu_views.xml",
        "views/hr_contract.hr_contract_view_for.xml",
        "views/report_contract.xml",
        "views/report_contract_template.xml",
        "views/dropdown_views.xml",
        "views/hr_recipe_manufacturing.xml",
        "data/allergen_category_data.xml",
        "views/stock_picking.xml",
        "views/product_template.xml",
        "wizard/product_wizard_view.xml",
        "views/portal_templates.xml",

    ],
    "demo": [

    ],
    'assets': {
        'web.assets_frontend': [
            'inscorp_custom_addon/static/src/js/allergen_update.js',
        ],
    },


    "installable": True,
    "auto_install": False,
}

# TODO:
# Pycharm etudiant OK
## Creer un formulaire bootstrap 5 sur le produit 1 etape:
### afficher un bouton OK + un champs selection qui reprends l'ensnbles des allerge sauf ceux qui sont déjà présent. OK
### créer une route update/allergen FAIT
### modifier l'affichage des alerge pour les rendrer avec un bouton supprimable (seulement pout les admins) OK
### créer une route de suppression.FAIT
### mail laurent : laurent.scheepers@dynapps.be IMPOSSIBLE MAIL BLOQUÉ
