import React from 'react';
import { Link } from 'react-router-dom';


const ButtonMenu = () => {
  
  return (
    <div className="sticky top-0 w-full bg-stone-800 py-4 text-white" >
      <ul className='flex justify-center content-center gap-4'>
        <li className='text-white px-2 py-1 hover:text-white transition duration-300' ><Link to="/registrar">Registrar</Link></li>
        <li className='text-white px-2 py-1 hover:text-white transition duration-300' ><Link to="/consultar">Consultar</Link></li>
        <li className='text-white px-2 py-1 hover:text-white transition duration-300' ><Link to="/agenda">Agenda</Link></li>
      </ul>
    </div>
  );
};


export default ButtonMenu;

