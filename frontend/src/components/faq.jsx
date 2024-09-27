import React from "react";
import step1Image from "./../assets/home.jpg"; // Replace with your actual image paths
import step2Image from "./../assets/home.jpg";
import step3Image from "./../assets/home.jpg";
import step4Image from "./../assets/home.jpg";

const steps = [
  {
    step: "Step 1: Scan your cube.",
    image: step1Image,
  },
  {
    step: "Step 2: Turn your cube as directed to scan all 6 faces.",
    image: step2Image,
  },
  {
    step: "Step 3: Follow the steps provided by Rubixx.",
    image: step3Image,
  },
  {
    step: "More steps...",
    image: step3Image,
  },
  {
    step: "More steps...",
    image: step3Image,
  },
  {
    step: "Congrats! You just solved your first Rubik's Cube!",
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
