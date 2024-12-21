import React, { useRef } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Faq from "./components/faq";
import Banner from "./components/banner";
import Quiz from "./components/quiz";
import Nav from "./components/nav";
import Solve from "./components/solve";

const App = () => {
  const faqRef = useRef(null);
  const quizRef = useRef(null);
  const solveRef = useRef(null);

  const scrollToFAQ = () => {
    faqRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const scrollToQuiz = () => {
    quizRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const scrollToSolve = () => {
    solveRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  return (
    <Router>
      <div className="bg-black">
        <Nav
          onFAQClick={scrollToFAQ}
          onQuizClick={scrollToQuiz}
          onSolveCLick={scrollToSolve}
        />
        <Routes>
          <Route path="/" element={<Banner />} />
          <Route
            path="/solve"
            element={
              <div ref={solveRef} className="section">
                <Solve />
              </div>
            }
          />
        </Routes>

        <div ref={faqRef} className="section">
          <Faq />
        </div>

        <div ref={quizRef} className="section">
          <Quiz />
        </div>
      </div>
    </Router>
  );
};

export default App;
