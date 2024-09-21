import React from 'react';

const AcessorioForm = () => {
  return (
    <form className="w-full text-nowrap bg-slate-600 shadow-md rounded px-8 pt-6 pb-8 mb-4">
      
      {/* Tipo */}
      <div className="mb-4">
        <label className="block text-left mb-2" htmlFor="tipo">Tipo:</label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-slate-200 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="tipo"
          name="tipo"
        />
      </div>

      {/* Tamanho */}
      <div className="mb-4">
        <label className="block text-left mb-2" htmlFor="tamanho">Tamanho:</label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-slate-200 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="tamanho"
          name="tamanho"
        />
      </div>

      {/* Cor */}
      <div className="mb-4">
        <label className="block text-left mb-2" htmlFor="cor">Cor:</label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-slate-200 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="cor"
          name="cor"
        />
      </div>

      {/* Status */}
      <div className="mb-4">
        <label className="block text-left mb-2" htmlFor="status">Status:</label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-slate-200 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="status"
          name="status"
        />
      </div>

      <button className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
      Enviar
    </button>
    </form>
  );
};

export default AcessorioForm;
