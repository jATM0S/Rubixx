import React, { useRef, useEffect, useState } from "react";
import "./cube.css";
import Cube from "./cube";
import CameraPopup from "./CameraPopUp";

const Solve = ({ onClose }) => {
  const [popupOpen, setPopupOpen] = useState(false);
  const [popupVisible, setVisibility] = useState(false);

  //selected color to fill
  const [currentColor, setCurrentColor] = useState("bg-white");

  const initialFaceColors = Array(9).fill("bg-white"); // Initial colors for each face
  const [cubeColors, setCubeColors] = useState({
    front: [...initialFaceColors],
    back: [...initialFaceColors],
    left: [...initialFaceColors],
    right: [...initialFaceColors],
    top: [...initialFaceColors],
    bottom: [...initialFaceColors],
  });
  const [response, setResponse] = useState({
    sequence: [],
    is_solved: true,
    error: "",
  });

  const getRubiks_cube = (cubeColors) => {
    const faces = ["F", "B", "L", "R", "U", "D"];
    const getColorNotation = {
      "bg-blue-600": "B",
      "bg-white": "W",
      "bg-green-500": "G",
      "bg-red-500": "R",
      "bg-orange-500": "O",
      "bg-yellow-400": "Y",
    };
    console.log(cubeColors);
    const rubiks_cube_notation = {};

    Object.keys(cubeColors).forEach((face, faceNo) => {
      cubeColors[face].forEach((color, index) => {
        rubiks_cube_notation[`${faces[faceNo]}${index + 1}`] =
          getColorNotation[color];
      });
    });
    return rubiks_cube_notation;
  };

  // fetch the solution and put in stateful variable
  const solve_cube = async () => {
    try {
      const cube = getRubiks_cube(cubeColors);
      console.log(cube);
      const response = await fetch("http://127.0.0.1:8000/solve/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          rubiks_cube: cube,
        }),
      });
      const data = await response.json();
      console.log(data);
      setResponse(data);
    } catch (error) {
      setResponse((prev) => {
        [], false, "Fetch error";
      });
    }
  };

  return (
    <div className="py-16 bg-blue-400">
      <div className="flex justify-evenly flex-wrap bg-blue-600">
        {/*cube */}
        <Cube
          cubeColors={cubeColors}
          currentColor={currentColor}
          setCubeColors={setCubeColors}
        />


        {/* menu */}
        <div className="flex flex-col justify-center bg-white w-auto">
          <button
            onClick={() => setPopupOpen(true)}
            className="bg-blue-600 text-white py-2 px-6 my-2 rounded hover:bg-blue-700 transition duration-300"
          >
            Scan the Cube
          </button>


          {popupOpen && (
            <CameraPopup
              onClose={() => setPopupOpen(false)}
              setCubeColors={setCubeColors}
            />
          )}

          {/* fillcube colors section */}
          <div className="my-2">
            <p className=" text-white font-bold text-lg select-none my-2 px-3 ">
              Fill Cube:
            </p>

            {/* colors */}
            <div
              className={`${currentColor} border-2 border-black p-3 mb-2 rounded-3xl flex align-middle justify-center flex-wrap`}
            >
              <div className="">
                <div
                  className="bg-blue-600 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-blue-600");
                  }}
                ></div>
                <div
                  className="bg-green-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-green-500");
                  }}
                ></div>
                <div
                  className="bg-red-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-red-500");
                  }}
                ></div>
              </div>
              <div className="">
                <div
                  className="bg-orange-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-orange-500");
                  }}
                ></div>
                <div
                  className="bg-yellow-400 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-yellow-400");
                  }}
                ></div>
                <div
                  className="bg-white border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                  onClick={() => {
                    setCurrentColor("bg-white");
                  }}
                ></div>
              </div>
              <div
                className="py-4 bg-gray-500 text-white select-none h-14 w-14 rounded-2xl mx-2 text-center"
                onClick={() => {
                  setCurrentColor("bg-white");
                  setCubeColors((prevColors) => {
                    const updatedColors = { ...prevColors };
                    const faces = [
                      "front",
                      "back",
                      "left",
                      "right",
                      "top",
                      "bottom",
                    ];
                    faces.forEach((face) => {
                      updatedColors[face] = [...initialFaceColors];
                    });
                    return updatedColors;
                  });
                }}
              >
                Clear
              </div>
            </div>
          </div>

          {/* sends the cube notation to solve */}
          <button
            onClick={solve_cube}
            className="bg-blue-600 text-white py-2 px-6 my-2 rounded hover:bg-blue-700 transition duration-300"
          >
            Solve the Cube
          </button>
        </div>
      </div>



      <div className="">
        <p className="text-white">
          {response.sequence?.length > 0
            ? response.sequence.join(" ")
            : response.error}
        </p>
      </div>
    </div>
  );
};
export default Solve;
