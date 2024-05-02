/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import {_t} from "@web/core/l10n/translation";

publicWidget.registry.AllergenUpdate = publicWidget.Widget.extend({
    selector: '.inscorp_allergen',
    events: {
        'click .allergen_delete': '_onDeleteBtnClick',
        'click .allergen_add': '_onAddBtnClick',
    },

    init() {
        this.rpc = this.bindService("rpc");
        console.log('Bonjour');
    },

    /**
     * @override
     */
    start: function () {
        console.log("start");
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _onDeleteBtnClick: async function (ev) {
        console.log(ev);
        // const deleteButton = this.$el.find(".allergen_delete");
        let productId = ev.currentTarget.getAttribute('productId');
        let allergenId = ev.currentTarget.getAttribute('allergenId');

        let reponse = await this.rpc("/delete_allergen",
            {
                product_id: productId,
                allergen_id: allergenId,
            }
        );
        if (reponse) {
            ev.currentTarget.parentElement.parentElement.remove();
        }

    },

    _onAddBtnClick: async function (ev) {
        console.log(ev);
        let productId = ev.currentTarget.getAttribute('productId');
        let allergenId = ev.currentTarget.getAttribute('allergenId');

        let reponse = await this.rpc("/add_allergen",
            {
                product_id: productId,
                allergen_id: allergenId,
            }
        );
        if (reponse) {
            ev.currentTarget.parentElement
        } else {
            ev.currentTarget.parentElement.remove();
        }

    },
});

export default publicWidget.registry.AllergenUpdate;