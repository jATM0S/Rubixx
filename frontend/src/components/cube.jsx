import React, { useState } from "react";
import "./cube.css";

const Cube = ({ cubeColors, currentColor, setCubeColors }) => {
  const [typeOfCube, setType] = useState("3d");
  const [rotation, setRotation] = useState({ y: -30, z: 0 });
  const [hidden, setHidden] = useState(false);

  return (
    <div className={`w-2/4 h-[500px] flex flex-col justify-center opacity-100 bg-green-300 transition-opacity duration-1000	`}>
      <div className="w-full flex justify-center ">
        <div className="flex justify-evenly w-56 ">
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300 "
            onClick={() => {
              setType("3d");
              setRotation((prev) => ({ y: -30, z: 0 }));
              setHidden(false);
            }}
          >
            3d
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300 active:bg-blue-700"
            onClick={() => {
              setType("2d");
              setRotation((prev) => ({ y: 0, z: 0 }));
              setHidden(true);
            }}
          >
            2d
          </button>
        </div>
      </div>

      <div
        className={`${
          typeOfCube == "3d" ? "h-[381px]" : "h-[430px]"
        } w-full flex justify-center items-center`}
      >
        <div
          className={`cube${typeOfCube} w-2 h-2`}
          style={{
            transform: `rotateX(-30deg) rotateY(${rotation.y}deg) rotateZ(${rotation.z}deg)`,
          }}
        >
          <div
            className={`face${typeOfCube} front${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none`}
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
                  {index + 1}F
                </div>
              ))}
          </div>
          <div
            className={`face${typeOfCube} back${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none `}
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
                  {index + 1}B
                </div>
              ))}
          </div>
          <div
            className={`face${typeOfCube} left${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none`}
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
                  {index + 1}L
                </div>
              ))}
          </div>
          <div
            className={`face${typeOfCube} right${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none`}
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
                  {index + 1}R
                </div>
              ))}
          </div>
          <div
            className={`face${typeOfCube} top${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none`}
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
                  {index + 1}T
                </div>
              ))}
          </div>
          <div
            className={`face${typeOfCube} bottom${typeOfCube} grid grid-cols-3 gap-0 border-2 select-none`}
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
                  {index + 1}B
                </div>
              ))}
          </div>
        </div>
      </div>

      <div
        className={`${
          hidden ? "hidden" : ""
        } flex justify-center align-middle `}
      >
        <div
          className="bg-blue-600 w-16 h-12"
          onClick={() => setRotation((prev) => ({ y: prev.y - 90, z: prev.z }))}
        ></div>
        <div
          className="bg-orange-600 w-16 h-12"
          onClick={() =>
            setRotation((prev) => ({ y: prev.y, z: prev.z - 180 }))
          }
        ></div>

        <div
          className="bg-blue-600 w-16 h-12"
          onClick={() => setRotation((prev) => ({ y: prev.y + 90, z: prev.z }))}
        ></div>
      </div>
    </div>
  );
};
export default Cube;
