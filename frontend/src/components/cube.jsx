import React, { useState } from "react";
import "./cube.css";
import eye from "./../assets/eye.png";

const Cube = ({ cubeColors, currentColor, setCubeColors }) => {
  const [typeOfCube, setType] = useState("3d");
  // const [hidden, setHidden] = useState(true);
  return (
    <div className={` w-2/4 h-[510px]`}>
      <div className="w-full flex justify-center ">
        <div className="flex justify-evenly w-56 ">
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
            onClick={() => setType("3d")}
          >
            3d
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300 active:bg-blue-700"
            onClick={() => setType("2d")}
          >
            2d
          </button>
        </div>
      </div>

      <div
        className={`${
          typeOfCube == "3d" ? "h-96" : "h-[480px]"
        } w-full flex justify-center `}
      >
        <div className={`cube${typeOfCube}`}>
          <div
            className={`face${typeOfCube} front${typeOfCube} grid grid-cols-3 gap-0 border-2 `}
          >
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
          <div
            className={`face${typeOfCube} back${typeOfCube} grid grid-cols-3 gap-0 border-2`}
          >
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
          <div
            className={`face${typeOfCube} left${typeOfCube} grid grid-cols-3 gap-0 border-2`}
          >
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
          <div
            className={`face${typeOfCube} right${typeOfCube} grid grid-cols-3 gap-0 border-2`}
          >
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
          <div
            className={`face${typeOfCube} top${typeOfCube} grid grid-cols-3 gap-0 border-2`}
          >
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
          <div
            className={`face${typeOfCube} bottom${typeOfCube} grid grid-cols-3 gap-0 border-2`}
          >
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
