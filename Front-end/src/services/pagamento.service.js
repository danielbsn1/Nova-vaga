import api from './api'

export const pagamentoService = {
  createCheckout: async (planoId) => {
    const { data } = await api.post('/pagamentos/checkout', { planoId })
    return data
  },

  verifyPayment: async (sessionId) => {
    const { data } = await api.get(`/pagamentos/verify/${sessionId}`)
    return data
  }
}
