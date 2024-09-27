import React, { useRef } from "react";
import Faq from "./components/faq";
import Banner from "./components/banner";
import Quiz from "./components/quiz";
import Nav from "./components/nav";

const App = () => {
  const faqRef = useRef(null);
  const quizRef = useRef(null);
  const scanRef = useRef(null);

  const scrollToFAQ = () => {
    faqRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const scrollToQuiz = () => {
    quizRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  const scrollToScan = () => {
    scanRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div>
      <Nav
        onFAQClick={scrollToFAQ}
        onQuizClick={scrollToQuiz}
        onScanClick={scrollToScan}
      />

      <div ref={scanRef} className="section">
        <Banner />
      </div>

      <div ref={faqRef} className="section">
        <Faq />
      </div>

      <div ref={quizRef} className="section">
        <Quiz />
      </div>
    </div>
  );
};

export default App;
