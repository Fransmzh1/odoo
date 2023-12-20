from odoo import http

class MyAPI(http.Controller):

    @http.route('/api/products', auth='public', methods=['GET'])
    def list_products(self, **kw):
        products = http.request.env['product.template'].search([])
        return http.request.render('my_module.products_template', {'products': products})
