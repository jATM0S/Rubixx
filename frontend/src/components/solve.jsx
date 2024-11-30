import React, { useRef, useEffect, useState } from "react";
import "./cube.css";

const Solve = ({ onClose }) => {
  const [response, setResponse] = useState({
    sequence: [],
    is_solved: true,
    error: "",
  });
  const [cubeNotation, setCubeNotation] = useState({
    F1: "",
    F2: "",
    F3: "",
    F4: "",
    F5: "",
    F6: "",
    F7: "",
    F8: "",
    F9: "",
    R1: "",
    R2: "",
    R3: "",
    R4: "",
    R5: "",
    R6: "",
    R7: "",
    R8: "",
    R9: "",
    B1: "",
    B2: "",
    B3: "",
    B4: "",
    B5: "",
    B6: "",
    B7: "",
    B8: "",
    B9: "",
    L1: "",
    L2: "",
    L3: "",
    L4: "",
    L5: "",
    L6: "",
    L7: "",
    L8: "",
    L9: "",
    U1: "",
    U2: "",
    U3: "",
    U4: "",
    U5: "",
    U6: "",
    U7: "",
    U8: "",
    U9: "",
    D1: "",
    D2: "",
    D3: "",
    D4: "",
    D5: "",
    D6: "",
    D7: "",
    D8: "",
    D9: "",
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
    <div className="">
      <div className="bg-black p-8 rounded shadow-lg text-center">
        <div className="w-full my-20 bg-black flex justify-center">
          {/* 3d cube */}
          <div class=" w-48 h-48 ">
            <div class="cube">
              <div class="face front bg-red-500">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
              <div class="face back bg-orange-500">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
              <div class="face left bg-blue-500">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
              <div class="face right bg-green-500">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
              <div class="face top bg-yellow-500">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
              <div class="face bottom bg-white">
                <div className="grid grid-cols-3 gap-0 w-48 h-48 border-2 border-black">
                  {Array(9)
                    .fill(null)
                    .map((_, index) => (
                      <div
                        key={index}
                        className="w-full h-full border border-black bg-white"
                      ></div>
                    ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        <button
          // onClick={}
          className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
        >
          Input cube string
        </button>

        {/* input cube string */}
        <form action="POST" className="hidden">
          <label
            htmlFor="cubeString  "
            className="text-slate-200 text-xl font-bold "
          >
            Cube string:{" "}
          </label>
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
          <input
            type="text"
            className="h-14 w-96 text-lg tracking-widest text-slate-200  bg-blue-500 p-3 rounded-lg"
          />
        </form>

        {/* sends the cube notation to solve */}
        <button
          onClick={solve_cube}
          className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
        >
          Solve the Cube
        </button>
        <p className="text-white">{response.sequence.join(" ")}</p>
        {/* <p>{response.sequence}</p> */}
      </div>
    </div>
  );
};
export default Solve;
