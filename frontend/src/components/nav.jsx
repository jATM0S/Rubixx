import React from "react";

const Nav = ({ onFAQClick, onQuizClick, onScanClick }) => {
  return (
    <div className="h-full w-full bg-black ">
      <nav className="flex justify-end p-4 pb-6 md:fixed w-full bg-transparent pr-12">
        <button
          onClick={onScanClick}
          className="text-white font-bold py-2 px-4 rounded"
        >
          Scan
        </button>
        <button
          onClick={onFAQClick}
          className="text-white font-bold py-2 px-4 rounded"
        >
          How to Use
        </button>
        <button
          onClick={onQuizClick}
          className="text-white font-bold py-2 px-4 rounded"
        >
          Quiz
        </button>
      </nav>
    </div>
  );
};

export default Nav;
