from odoo import fields, http
from odoo.http import request
import odoo
from odoo.exceptions import AccessError, UserError, AccessDenied
from odoo.addons.website_sale.controllers.main import WebsiteSale


# class AuthSignupHome(Home):

    # @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    # def web_auth_signup(self, *args, **kw):
    #     qcontext = self.get_auth_signup_qcontext()
    #
    #     if not qcontext.get('token') and not qcontext.get('signup_enabled'):
    #         raise werkzeug.exceptions.NotFound()
    #     cust = request.env['ir.config_parameter'].sudo().search(
    #         [('key', '=', 'website_terms_conditions.is_terms_and_conditions')])
    #     # cust=request.env["res.config.settings"].sudo().search([("is_terms_and_conditions", "=", True)])
    #     if cust:
    #         cust.value = True
    #         qcontext['enable1'] = True
    #     if 'error' not in qcontext and request.httprequest.method == 'POST':
    #         try:
    #             self.do_signup(qcontext)
    #             # Send an account creation confirmation email
    #             if qcontext.get('token'):
    #                 User = request.env['res.users']
    #                 user_sudo = User.sudo().search(
    #                     User._get_login_domain(qcontext.get('login')), order=User._get_login_order(), limit=1
    #                 )
    #                 template = request.env.ref('auth_signup.mail_template_user_signup_account_created',
    #                                            raise_if_not_found=False)
    #                 if user_sudo and template:
    #                     template.sudo().send_mail(user_sudo.id, force_send=True)
    #             return self.web_login(*args, **kw)
    #         except UserError as e:
    #             qcontext['error'] = e.args[0]
    #         except (SignupError, AssertionError) as e:
    #             if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
    #                 qcontext["error"] = _("Another user is already registered using this email address.")
    #             else:
    #                 _logger.error("%s", e)
    #                 qcontext['error'] = _("Could not create a new account.")
    #
    #     response = request.render('auth_signup.signup', qcontext)
    #     response.headers['X-Frame-Options'] = 'DENY'
    #     return response

