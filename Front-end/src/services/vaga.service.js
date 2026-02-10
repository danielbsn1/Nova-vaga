import api from './api'

export const vagaService = {
  getAll: async () => {
    const { data } = await api.get('/vagas')
    return data
  },

  getById: async (id) => {
    const { data } = await api.get(`/vagas/${id}`)
    return data
  },

  create: async (vagaData) => {
    const { data } = await api.post('/vagas', vagaData)
    return data
  },

  update: async (id, vagaData) => {
    const { data } = await api.put(`/vagas/${id}`, vagaData)
    return data
  },

  delete: async (id) => {
    await api.delete(`/vagas/${id}`)
  }
}
