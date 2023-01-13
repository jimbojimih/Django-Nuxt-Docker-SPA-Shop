export const state = () => ({
  cart_total: 0
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
    state.cart_total = 0
  },
}