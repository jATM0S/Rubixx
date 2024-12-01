import React, { useRef, useEffect, useState } from "react";
import "./cube.css";

const Solve = ({ onClose }) => {
  const [currentColor, setCurrentColor] = useState("bg-white");
  const [response, setResponse] = useState({
    sequence: [],
    is_solved: true,
    error: "",
  });
  const initialFaceColors = Array(9).fill("bg-white"); // Initial colors for each face
  const [cubeColors, setCubeColors] = useState({
    front: [...initialFaceColors],
    back: [...initialFaceColors],
    left: [...initialFaceColors],
    right: [...initialFaceColors],
    top: [...initialFaceColors],
    bottom: [...initialFaceColors],
  });

  // fetch the solution and put in stateful variable
  const solve_cube = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/solve/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          rubiks_cube: {
            F1: "O",
            F2: "R",
            F3: "O",
            F4: "Y",
            F5: "R",
            F6: "O",
            F7: "B",
            F8: "Y",
            F9: "Y",
            R1: "G",
            R2: "O",
            R3: "B",
            R4: "B",
            R5: "G",
            R6: "B",
            R7: "G",
            R8: "G",
            R9: "W",
            B1: "O",
            B2: "Y",
            B3: "W",
            B4: "W",
            B5: "O",
            B6: "O",
            B7: "R",
            B8: "O",
            B9: "O",
            L1: "R",
            L2: "R",
            L3: "G",
            L4: "W",
            L5: "B",
            L6: "G",
            L7: "Y",
            L8: "R",
            L9: "R",
            U1: "B",
            U2: "B",
            U3: "W",
            U4: "W",
            U5: "Y",
            U6: "G",
            U7: "Y",
            U8: "B",
            U9: "W",
            D1: "Y",
            D2: "R",
            D3: "R",
            D4: "G",
            D5: "W",
            D6: "W",
            D7: "B",
            D8: "Y",
            D9: "G",
          },
        }),
      });
      const data = await response.json();
      console.log(data);
      setResponse(data);
    } catch (error) {
      setResponse([[], false, "Fetch error"]);
    }
  };

  return (
    <div className="bg-black p-6 flex justify-evenly ">
      {/* 3d cube */}
      <div class="cube m-20 w-56 h-56">
        <div class="face front ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black ">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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
        </div>
        <div class="face back ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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
        </div>
        <div class="face left ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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
        </div>
        <div class="face right ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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
        </div>
        <div class="face top ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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
        </div>
        <div class="face bottom ">
          <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
            {Array(9)
              .fill(null)
              .map((_, index) => (
                <div
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

      {/* menu */}
      <div className=" flex flex-col justify-center">
        {/* fillcube section */}
        <div className="my-3">
          <p className=" text-white font-bold text-lg select-none py-2 px-3">Fill Cube:</p>

          {/* colors */}
          <div
            className={`${currentColor} border-2 border-black p-3 rounded-3xl flex align-middle justify-center`}
          >
            <div
              className="bg-blue-600 border-2 border-black h-14 w-14 rounded-2xl mx-2"
              onClick={() => {
                setCurrentColor("bg-blue-600");
              }}
            ></div>
            <div
              className="bg-red-500 border-2 border-black h-14 w-14 rounded-2xl mx-2"
              onClick={() => {
                setCurrentColor("bg-red-500");
              }}
            ></div>
            <div
              className="bg-orange-500 border-2 border-black h-14 w-14 rounded-2xl mx-2"
              onClick={() => {
                setCurrentColor("bg-orange-600");
              }}
            ></div>
            <div
              className="bg-yellow-400 border-2 border-black h-14 w-14 rounded-2xl mx-2"
              onClick={() => {
                setCurrentColor("bg-yellow-400");
              }}
            ></div>
            <div
              className="bg-white border-2 border-black h-14 w-14 rounded-2xl mx-2"
              onClick={() => {
                setCurrentColor("bg-white");
              }}
            ></div>
            <div
              className="py-4 bg-gray-500 text-white select-none h-14 w-14 rounded-2xl mx-2 text-center"
              onClick={() => {
                setCurrentColor("bg-white");
                setCubeColors((prevColors) => {
                  const updatedColors = { ...prevColors };
                  const faces=["front","back","left","right","top","bottom"]
                  faces.forEach((face)=>{updatedColors[face]= [...initialFaceColors];})
                  return updatedColors;
                })
              }}
            >
              Clear
            </div>
          </div>
        </div>

        {/* sends the cube notation to solve */}
        <button
          onClick={solve_cube}
          className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
        >
          Solve the Cube
        </button>
      </div>
      <p className="text-white">{response.sequence.join(" ")}</p>
    </div>
  );
};
export default Solve;
