import React, { useRef, useEffect, useState } from "react";
const Solve = ({ onClose }) => {
  return (
    <div className="mt-11">
      <div className="bg-white p-8 rounded shadow-lg text-center">
        <form action="POST">
          <label htmlFor="cubeString  " className="text-red-800">Cube string</label>
          <input type="text" />
        </form>

      </div>
    </div>
  );
};
export default Solve;
