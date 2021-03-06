odoo.define('login_as', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var _t = core._t;

    var LoginAs = Widget.extend({
        template: 'LoginAs',
        events: {
            'click a#login_as': 'login_as',
        },
        login_as: function(event) {
            event.preventDefault();
            var self = this;
            rpc.query({
                model: 'ir.ui.view',
                method: 'get_view_id',
                args: ['login_as_another_user.view_res_users_login_as_form'],
            }).then(function (view_id) {
                self.do_action({
                    type: 'ir.actions.act_window',
                    name: _t('Login as'),
                    views: [[view_id, 'form']],
                    res_model: 'res.users',
                    res_id: session.uid,
                    target: 'new',
                });
            });
        }
    });

    SystrayMenu.Items.push(LoginAs);

});
