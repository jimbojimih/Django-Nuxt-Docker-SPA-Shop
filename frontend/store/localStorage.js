export const state = () => ({
  cart_total: 0,
  first_name: '',
  email: '',
  city: '',
  street: '',
  house: '',
  number_phone: '',
  comments: '',
})

export const mutations = {
  add_cart_total (state) {
    state.cart_total++
  },
  remove_cart_total (state) {
    if (state.cart_total === 0)
      state.cart_total =0
    else
      state.cart_total--
  },

  clear_cart_total (state) {
    state.cart_total = 0;
    state.first_name = '';
    state.email = '';
    state.city = '';
    state.street = '';
    state.house = '';
    state.number_phone = '';
    state.comments = ''
  },

  set_form_value (state, payload) {
    let key = payload.key
    let value = payload.value
    state[key] = value
  },
}