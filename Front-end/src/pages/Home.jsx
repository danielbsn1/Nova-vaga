import React from "react";
import { useNavigate } from "react-router-dom";



const Home = () => {
    const navigate = useNavigate();
  return (
    <div>
      <h1>Bem-vindo à Nova Vaga</h1>
      <p>Escolha uma opção para continuar:</p>
      <div>
        <button onClick={() => navigate("/Login/Candidato")}>Candidato</button>
        <button onClick={() => navigate("/Login/Empresa")}>Empresa</button>
        <button onClick={() => navigate("/Cadastro/Empresa")}>Administrador</button>
        <button onClick={() => navigate("/Cadastro/Candidato")}>Cadastre-se</button>
      </div>
    </div>
  );
};

export default Home;