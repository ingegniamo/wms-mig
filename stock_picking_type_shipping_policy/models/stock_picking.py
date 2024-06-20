from odoo import api, fields, models,_
class Picking(models.Model):
    _inherit = "stock.picking"
    @api.model
    def default_get(self, fields):
        res = super(Picking, self).default_get(fields)
        if 'picking_type_id' in res and res.get('picking_type_id'):
            picking_type = self.env['stock.picking.type'].browse(res.get('picking_type_id'))
            move_type = False
            if picking_type.shipping_policy == "force_as_soon_as_possible":
                move_type =  "direct"
            elif picking_type.shipping_policy == "force_all_products_ready":
                move_type = "one"
            if move_type:
                res['move_type'] = move_type

       
        return res
