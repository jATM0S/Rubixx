// src/quizData.js
const questionsAndAnswers = [
  {
    question:
      "What is the maximum number of moves required to solve any solvable Rubik’s Cube configuration?",
    answer: "The maximum number of moves for a 3×3 Rubik’s Cube is 20 moves.",
  },
  {
    question:
      "Can a single move on a Rubik’s Cube change only one corner’s position without affecting the rest?",
    answer:
      "No, a single move affects multiple pieces. Every move involves turning one or more layers, thus affecting multiple pieces.",
  },
  {
    question:
      "What is the fewest number of moves ever recorded to solve a Rubik’s Cube officially?",
    answer: "In January 2022, the record was 3.47 seconds, held by Yusheng Du.",
  },
  {
    question:
      "How many possible combinations are there on a standard 3×3 Rubik’s Cube?",
    answer:
      "There are 43,252,003,274,489,856,000 possible combinations on a standard 3×3 Rubik’s Cube.",
  },
  {
    question: "Who invented the Rubik’s Cube?",
    answer: "Erno Rubik is the inventor of the Rubik’s Cube.",
  },
  {
    question: "Can you solve a Rubik’s Cube blindfolded? How is it done?",
    answer:
      "Yes, blindfold solving is possible using memorization techniques and algorithms.",
  },
  {
    question:
      "What is the term for a sequence of moves that, when repeated, returns a Rubik’s Cube to its original state?",
    answer:
      "A sequence of moves that repeats and restores the cube to its original state is called a 'repeating pattern' or 'cycle.'",
  },
  {
    question: "How many edges does a standard 3×3 Rubik’s Cube have?",
    answer: "A 3×3 Rubik’s Cube has 12 edges.",
  },
  {
    question:
      "What is the 'God's number' for the 3×3 Rubik’s Cube, and what does it represent?",
    answer:
      "God's number for the 3×3 Rubik’s Cube is 20. It represents the maximum number of moves needed to solve any solvable configuration.",
  },
  {
    question:
      "Can you name the six colors commonly found on a standard Rubik’s Cube?",
    answer: "The six colours are white, yellow, blue, green, red, and orange.",
  },
  {
    question:
      "What is the primary method used by speedcubers to solve the Rubik’s Cube quickly?",
    answer:
      "The CFOP (Cross, F2L, OLL, PLL) method is commonly used by speedcubers.",
  },
  {
    question:
      "What is the concept of parity in Rubik’s Cube solving, and how does it affect the solving process?",
    answer:
      "Parity refers to a situation where the cube appears to be unsolvable due to an odd number of piece swaps.",
  },
  {
    question:
      "What is a PLL (Permutation of the Last Layer) in Rubik’s Cube terminology?",
    answer:
      "PLL refers to the last step in the CFOP method, where the pieces on the last layer are permuted to their correct positions.",
  },
  {
    question:
      "How many different F2L (First Two Layers) cases are there in the CFOP method?",
    answer: "There are 41 different F2L cases in the CFOP method.",
  },
  {
    question:
      "Can you solve a 4×4 Rubik’s Cube using the same methods as a 3×3?",
    answer:
      "Yes, although additional techniques are needed for the parity cases that can occur on larger cubes.",
  },
  {
    question:
      "What is the term for a Rubik’s Cube pattern where only the corner pieces are twisted?",
    answer: "This is called a 'T perm' or 'corner permutation.'",
  },
  {
    question: "How many possible 2×2 Rubik’s Cube combinations are there?",
    answer: "There are 3,674,160 possible combinations on a 2×2 Rubik’s Cube.",
  },
  {
    question:
      "What is the purpose of the cross in the CFOP method for solving the Rubik’s Cube?",
    answer:
      "The cross is the first step in CFOP and involves solving a cross on one face.",
  },
  {
    question:
      "Can you name three different methods for solving a Rubik’s Cube?",
    answer: "Three methods include CFOP, Roux, and Petrus.",
  },
  {
    question:
      "What is the ZB method in Rubik’s Cube solving, and how does it differ from other methods?",
    answer:
      "The ZB method is an advanced method focusing on more efficient algorithms.",
  },
  {
    question: "How many pieces does a standard Rubik’s Cube have in total?",
    answer:
      "A standard 3×3 Rubik’s Cube has 54 stickers, representing 54 individual pieces.",
  },
  {
    question:
      "What is the world record for the fastest time to solve a 4×4 Rubik’s Cube, and who holds it?",
    answer: "The record was 17.42 seconds, held by Yusheng Du.",
  },
  {
    question:
      "What is the concept of lookahead in speedcubing, and why is it important?",
    answer:
      "Lookahead is the ability to plan the next moves while executing the current ones.",
  },
  {
    question:
      "Can you solve a Rubik’s Cube using only one hand? What is the one-handed world record?",
    answer:
      "Yes, one-handed solving is possible. The world record for one-handed solving was 6.82 seconds, held by Max Park.",
  },
  {
    question:
      "How does the concept of orientation and permutation apply to the solving of Rubik’s Cube?",
    answer:
      "Orientation refers to the way pieces are turned, while permutation refers to their arrangement.",
  },
];

export default questionsAndAnswers;
