import React from "react";
import ButtonMenu from "./ButtonMenu";

const Header = () => {
  return (
    <div className="sticky w-full text-center " style={{ background: 'linear-gradient(to right, #cea42e, #e4d494)' }}>
      <header className="flex max-w-7xl mx-auto items-center p-4 justify-between">
        <div className="flex items-center">
          <img
            className="w-20 h-30 drop-shadow-sm"
            src="img/logo.png"
            alt="Logo Milla Fashion"
          />
          
          {/* fonte customizada do google fonts bebas-neue-regular */}
          <h2 className="tracking-widest bebas-neue-regular text-left ml-6 text-2xl font-bold text-black">
            Sistema de locações Milla Fashion
          </h2>
        </div>
        <ButtonMenu className="w-auto text-left" />
      </header>
    </div>
  );
};

export default Header;
