import React from "react";
import { useNavigate } from "react-router-dom";

const Nav = ({
  onSolveClick = () => {},
  onFAQClick = () => {},
  onQuizClick = () => {},
}) => {
  const navigate = useNavigate();

  const navigateToSolve = () => {
    navigate("/solve");
    onSolveClick();
  };

  return (
    <nav className="flex justify-end p-4 pb-6 fixed w-full pr-12">
      <button
        onClick={navigateToSolve}
        className="text-white font-bold py-2 px-4 rounded"
      >
        Solve
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
  );
};

export default Nav;
