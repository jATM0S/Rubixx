import React from "react";
import step1 from "./../assets/step1.png";
import step2 from "./../assets/step2.png";
import step3Image from "./../assets/home.jpg";
import step4Image from "./../assets/home.jpg";

const steps = [
  {
    step: "Step 1: Select a suitable view (3D or 2D) for scanning. Ensure the system mirrors colors as you view them. Change the face above the camera to scan all sides.",
    image: step1,
  },
  {
    step: "Step 2: Save all scanned faces and verify the colors. Manually correct any errors caused by lighting.",
    image: step2,
  },
  {
    step: "Step 3: Confirm the setup, then click 'Solve the Cube.'",
    image: step3Image,
  },
  {
    step: "Step 4: Follow the on-screen steps to solve the cube.",
    image: step3Image,
  },
  {
    step: "Step 5: Congratulations! Your cube is solved. Note: Altered cubes may not be solvable.",
    image: step4Image,
  },
];

const Faq = () => {
  return (
    <div className="w-full h-full bg-no-repeat bg-black bg-center bg-contain flex flex-wrap justify-center gap-2 pb-12">
      <div className="text-white w-full text-center mb-8">
        <h1 className="text-5xl font-bold mb-4 mt-24 md:mt-12">
          How to use Rubixx?
        </h1>
        <p className="text-lg mb-4 text-justify md:text-center px-6 md:px-36 text-gray-400 ">
          Rubixx is designed to simplify the process of solving a Rubik's Cube.
          We understand that it can be challenging to navigate the various
          techniques, and our goal is to guide you through every step.
        </p>
      </div>
      {steps.map((item, index) => (
        <div
          key={index}
          className="flex flex-col items-center justify-around gap-2 rounded-2xl shadow-xl bg-blue-400 bg-opacity-25 p-4 mx-8 mb-8 w-full md:w-1/4"
        >
          <img
            src={item.image}
            alt={`Step ${index + 1}`}
            className="w-full h-40 object-contain mb-2"
          />
          <p className="text-center text-white">{item.step}</p>
        </div>
      ))}
    </div>
  );
};

export default Faq;
