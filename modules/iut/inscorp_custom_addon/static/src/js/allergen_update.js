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
    // deplacer observers a un niveau superieur
    // retravailler logique
    // lors de l'ajout en js
    /**
     * @private
     */
    _onDeleteBtnClick: async function (ev) {
        console.log(ev);
        // const deleteButton = this.$el.find(".allergen_delete");
        let productId = ev.currentTarget.getAttribute('productId');
        let allergenId = ev.currentTarget.getAttribute('allergenId');
        let select = document.getElementById('allergen_id');
        let option = document.createElement('option');
        // let name = select.textContent;
        let reponse = await this.rpc("/delete_allergen",
            {
                product_id: productId,
                allergen_id: allergenId,
            }
        );
        if (reponse) {

            ev.currentTarget.innerHTML
            option.id = allergenId;
            option.value = allergenId;
            option.setAttribute('selected', allergenId);
            // const text = document.querySelectorAll('span[id=allergenId]');
            // console.log(text.text);
            option.text = ev.currentTarget.parentElement.textContent;
            select.appendChild(option);
            ev.currentTarget.parentElement.remove()
        }

    },

    _onAddBtnClick: async function (ev) {
        console.log(ev);
        let select = document.getElementById('allergen_id');
        let productId = ev.currentTarget.getAttribute('productId');
        let allergenId = select.value;
        let inscorp = document.getElementById('test');
        let div = document.createElement('div');
        let allergenText = document.createElement('span');
        let trashButton = document.createElement('button');
        let selectedOption = select.options[select.selectedIndex];
        let selectedText = selectedOption.text;

        if (allergenId) {
            let reponse = await this.rpc("/add_allergen",
                {
                    product_id: productId,
                    allergen_id: allergenId,
                }
            );
            if (reponse) {
                allergenText.setAttribute('id', allergenId)
                allergenText.textContent = selectedText;
                allergenText.setAttribute('groups', 'base.group_erp_manager')
                document.getElementById(allergenId).remove()
                trashButton.setAttribute('allergenId', allergenId);
                trashButton.setAttribute('productId', productId);
                trashButton.type = 'button';
                trashButton.classList.add('fa');
                trashButton.classList.add('fa-trash');
                trashButton.classList.add('allergen_delete');
                trashButton.style.all = "unset"
                trashButton.style.cursor = "pointer"
                div.appendChild(allergenText);
                div.appendChild(trashButton);
                inscorp.appendChild(div);
            }
        }

    },
});

export default publicWidget.registry.AllergenUpdate;