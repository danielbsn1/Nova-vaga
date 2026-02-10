import { Routes, Route } from 'react-router-dom'
import PrivateRoute from './PrivateRoute'
import PublicRoute from './PublicRoute'
import Home from '../pages/Home'
import Login from '../pages/Login'
import Cadastro from '../pages/Cadastro'
import Vagas from '../pages/Vagas'
import VagaDetalhe from '../pages/VagaDetalhe'
import EmpresaDashboard from '../pages/EmpresaDashboard'
import NovaVaga from '../pages/NovaVaga'
import FreelancerDashboard from '../pages/FreelancerDashboard'
import Planos from '../pages/Planos'

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<PublicRoute><Login /></PublicRoute>} />
      <Route path="/cadastro" element={<PublicRoute><Cadastro /></PublicRoute>} />
      <Route path="/vagas" element={<Vagas />} />
      <Route path="/vagas/:id" element={<VagaDetalhe />} />
      <Route path="/planos" element={<Planos />} />
      <Route path="/empresa/dashboard" element={<PrivateRoute><EmpresaDashboard /></PrivateRoute>} />
      <Route path="/empresa/nova-vaga" element={<PrivateRoute><NovaVaga /></PrivateRoute>} />
      <Route path="/freelancer/dashboard" element={<PrivateRoute><FreelancerDashboard /></PrivateRoute>} />
    </Routes>
  )
}
