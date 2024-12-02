import React, { useState } from "react";
import "./cube.css";

const Cube = ({ cubeColors, currentColor, setCubeColors }) => {
  const [typeOfCube, setType] = useState("");
  return (
    <div className="bg-white flex flex-col justify-center">
      <div className="flex justify-evenly ">
        <button className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300">
          3d
        </button>
        <button className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300">
          2d
        </button>
      </div>
      <div className=" bg-green-400 w-80 h-80 flex justify-center items-center pt-10">
        <div className="cube w-56 h-56">
          <div className="face front grid grid-cols-3 gap-0 border-2">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`front-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.front[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.front[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
          <div className="face back grid grid-cols-3 gap-0 border-2 ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`back-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.back[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.back[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
          <div className="face left grid grid-cols-3 gap-0 border-2 ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`left-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.left[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.left[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
          <div className="face right grid grid-cols-3 gap-0 border-2 ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`right-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.right[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.right[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
          <div className="face top grid grid-cols-3 gap-0 border-2 ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`top-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.top[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.top[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
          <div className="face bottom grid grid-cols-3 gap-0 border-2 ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
                  key={`bottom-${index}`}
                  className={`w-full h-full border border-black ${cubeColors.bottom[index]}`}
                  onClick={() =>
                    setCubeColors((prevColors) => {
                      const updatedColors = { ...prevColors };
                      updatedColors.bottom[index] = currentColor;
                      return updatedColors;
                    })
                  }
                >
                  {index + 1}
                </div>
              ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default Cube;
