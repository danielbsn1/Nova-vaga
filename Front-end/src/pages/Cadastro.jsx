import React from 'react';
import { useState } from 'react';

const Cadastro = () => {

   const [tipo, setTipo] = useState ("Candidato"); 

   return (

    <form>
      <select value={tipo} onChange={(e) => setTipo(e.target.value)}>
        <option value="candidato">Candidato</option>
        <option value="empresa">Empresa</option>
      </select>

      <input type="text" placeholder="Nome" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Senha" />

      {tipo === "empresa" && <input type="text" placeholder="CNPJ" />}
      {tipo === "candidato" && <input type="text" placeholder="Currículo" />}

      <button type="submit">Cadastrar</button>
    </form>
  );
};
 
export default Cadastro;