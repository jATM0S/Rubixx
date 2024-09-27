import React, { useState } from "react";
import questionsAndAnswers from "./../data/quizData";
import faq from "./../assets/faq.mp4";

const Quiz = () => {
  const [currentQuestion, setCurrentQuestion] = useState(getRandomQuestion());
  const [showAnswer, setShowAnswer] = useState(false);

  function getRandomQuestion() {
    return questionsAndAnswers[
      Math.floor(Math.random() * questionsAndAnswers.length)
    ];
  }

  const handleNewQuestion = () => {
    setCurrentQuestion(getRandomQuestion());
    setShowAnswer(false);
  };

  return (
    <div className="w-full h-screen bg-no-repeat bg-black bg-center bg-contain p-[20px] pl-16 flex items-center gap-12">
      <div className="w-1/2 ">
        <video src={faq} autoPlay loop muted className="w-full h-auto" />
      </div>
      <div className="w-1/2 px-36 pb-16 rounded-2xl flex flex-col gap-12 shadow-lg">
        <div className="text-white text-center">
          <h1 className="text-3xl font-bold shadow-md rounded-2xl p-4 py-8 shadow-blue-200 mb-16">
            Do you know these facts about your Rubik's Cube?
          </h1>
          <button
            onClick={() => setShowAnswer(!showAnswer)}
            className={`rounded-2xl p-8 ${
              showAnswer
                ? "bg-blue-400 bg-opacity-75 shadow-md p-4 shadow-blue-400"
                : "bg-blue-900 bg-opacity-65 shadow-md shadow-blue-200"
            }`}
          >
            {showAnswer
              ? `Answers: ${currentQuestion.answer}`
              : currentQuestion.question}
          </button>
        </div>
        <button
          onClick={handleNewQuestion}
          style={{ marginTop: "20px" }}
          className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
        >
          Refresh Question
        </button>
      </div>
    </div>
  );
};

export default Quiz;
