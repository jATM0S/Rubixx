import React, { useState } from "react";
import home from "./../assets/home.jpg";
import CameraPopup from "./CameraPopUp";

const Banner = () => {
  const [popupOpen, setPopupOpen] = useState(false);

  return (
    <div className="w-full h-screen bg-cover bg-center bg-black">
      <div className="w-full h-full  md:inline-flex items-center">
        <div className="md:w-1/2 p-8 md:ml-6 text-center md:text-left">
          <h1 className="text-5xl font-bold text-white mb-4 mt-12 md:mt-0">
            Rubixx
          </h1>
          <p className="text-xl text-gray-300 mb-2">Rubik's Cube Solver</p>
          <p className="text-lg text-gray-400 mb-4">
            Our solver is designed to capture images of a Rubik's cube face,
            analyze them, and provide step-by-step instructions to solve it.
          </p>
          <p className="text-lg text-gray-300 mb-6">
            Want to solve your mixed-up cube? Let’s get started!
          </p>
          <button
            onClick={() => setPopupOpen(true)}
            className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
          >
            Scan the Cube
          </button>
        </div>
        <img
          src={home}
          alt="Rubik's Cube Solver"
          className="md:mt-24 md:w-1/2"
        />
      </div>

      {popupOpen && <CameraPopup onClose={() => setPopupOpen(false)} />}
    </div>
  );
};

export default Banner;
