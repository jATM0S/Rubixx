import React, { useRef, useEffect, useState } from "react";

const CameraPopup = ({ onClose }) => {
  const videoRef = useRef(null);
  const mediaStreamRef = useRef(null);
  const [results, setResults] = useState([]);
  const [inputFace, setFace] = useState("front");
  const topRef = useRef(null);
  const leftRef = useRef(null);
  const frontRef = useRef(null);
  const rightRef = useRef(null);
  const backRef = useRef(null);
  const bottomRef = useRef(null);

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        mediaStreamRef.current = stream;
        videoRef.current.onloadedmetadata = () => {
          videoRef.current.play().catch((error) => {
            console.error("Error playing video: ", error);
          });
        };
        // videoRef.current.play();
        console.log("Camera started successfully.");
      }
    } catch (error) {
      console.error("Error accessing the camera: ", error);
    }
  };

  const stopCamera = () => {
    if (mediaStreamRef.current) {
      mediaStreamRef.current.getTracks().forEach((track) => track.stop());
      mediaStreamRef.current = null;
      if (videoRef.current) {
        videoRef.current.srcObject = null;
      }
      console.log("Camera stopped.");
    }
  };

  const squares = [
    { x: 150, y: 100, size: 30 },
    { x: 250, y: 100, size: 30 },
    { x: 350, y: 100, size: 30 },
    { x: 150, y: 200, size: 30 },
    { x: 250, y: 200, size: 30 },
    { x: 350, y: 200, size: 30 },
    { x: 150, y: 300, size: 30 },
    { x: 250, y: 300, size: 30 },
    { x: 350, y: 300, size: 30 },
  ];
  const analyzeFrame = async () => {
    if (videoRef.current) {
      const videoWidth = videoRef.current.videoWidth;
      const videoHeight = videoRef.current.videoHeight;

      const canvas = document.createElement("canvas");
      canvas.width = videoWidth;
      canvas.height = videoHeight;
      const context = canvas.getContext("2d", { willReadFrequently: true });

      // Draw the video frame on the canvas
      context.drawImage(videoRef.current, 0, 0, videoWidth, videoHeight);

      // Adjust squares to match video dimensions
      const adjustedSquares = squares.map(({ x, y, size }) => ({
        x: x * (videoWidth / videoRef.current.offsetWidth), // Scale to videoWidth
        y: y * (videoHeight / videoRef.current.offsetHeight), // Scale to videoHeight
        size: size * (videoWidth / videoRef.current.offsetWidth), // Scale size
      }));

      const croppedImages = adjustedSquares.map(({ x, y, size }) => {
        const imageData = context.getImageData(x, y, size, size); // Crop square
        const cropCanvas = document.createElement("canvas"); // Create a new canvas for each crop
        cropCanvas.width = size;
        cropCanvas.height = size;
        const cropContext = cropCanvas.getContext("2d");
        cropContext.putImageData(imageData, 0, 0); // Paste the cropped image onto the new canvas
        return cropCanvas.toDataURL("image/png"); // Default is "image/png"
      });

      const response = await fetch("http://127.0.0.1:8000/scan/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ face: croppedImages }),
      });

      const data = await response.json();
      setResults(data);
    }
  };

  useEffect(() => {
    startCamera();
    frontRef.current.focus();
    // const intervalId = setInterval(analyzeFrame, 1000); // Analyze every second

    return () => {
      // clearInterval(intervalId);
      stopCamera(); // Cleanup on component unmount
    };
  }, []);

  return (
    <div className="absolute flex items-center justify-center mt-5">
      <div className="bg-white p-3 rounded shadow-lg">
        {/* face to input section */}
        <div className="flex justify-center items-center">
          <span className=" text-black text-2xl mx-4">Face:</span>
          <div className="grid grid-cols-4 grid-rows-3 gap-1 h-16 w-24">
            <div
              className={`col-start-2 col-span-1 row-start-1 row-span-1 border-2 border-black ${
                inputFace == "top" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("top");
              }}
              tabIndex={0}
              ref={topRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  bottomRef.current.focus();
                  setFace("bottom");
                } else if (event.key === "ArrowDown") {
                  frontRef.current.focus();
                  setFace("front");
                } else if (event.key === "ArrowLeft") {
                  leftRef.current.focus();
                  setFace("left");
                } else if (event.key === "ArrowRight") {
                  rightRef.current.focus();
                  setFace("right");
                }
              }}
            ></div>
            <div
              className={`col-start-1 col-span-1 row-start-2 row-span-1 border-2 border-black ${
                inputFace == "left" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("left");
              }}
              tabIndex={0}
              ref={leftRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  topRef.current.focus();
                  setFace("top");
                } else if (event.key === "ArrowDown") {
                  bottomRef.current.focus();
                  setFace("bottom");
                } else if (event.key === "ArrowLeft") {
                  backRef.current.focus();
                  setFace("back");
                } else if (event.key === "ArrowRight") {
                  frontRef.current.focus();
                  setFace("front");
                }
              }}
            ></div>
            <div
              className={`col-start-2 col-span-1 row-start-2 row-span-1 border-2 border-black ${
                inputFace == "front" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("front");
              }}
              tabIndex={0}
              ref={frontRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  topRef.current.focus();
                  setFace("top");
                } else if (event.key === "ArrowDown") {
                  bottomRef.current.focus();
                  setFace("bottom");
                } else if (event.key === "ArrowLeft") {
                  leftRef.current.focus();
                  setFace("left");
                } else if (event.key === "ArrowRight") {
                  rightRef.current.focus();
                  setFace("right");
                }
              }}
            ></div>
            <div
              className={`col-start-3 col-span-1 row-start-2 row-span-1 border-2 border-black ${
                inputFace == "right" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("right");
              }}
              tabIndex={0}
              ref={rightRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  topRef.current.focus();
                  setFace("top");
                } else if (event.key === "ArrowDown") {
                  bottomRef.current.focus();
                  setFace("bottom");
                } else if (event.key === "ArrowLeft") {
                  frontRef.current.focus();
                  setFace("front");
                } else if (event.key === "ArrowRight") {
                  backRef.current.focus();
                  setFace("back");
                }
              }}
            ></div>
            <div
              className={`col-start-4 col-span-1 row-start-2 row-span-1 border-2 border-black ${
                inputFace == "back" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("back");
              }}
              tabIndex={0}
              ref={backRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  topRef.current.focus();
                  setFace("top");
                } else if (event.key === "ArrowDown") {
                  bottomRef.current.focus();
                  setFace("bottom");
                } else if (event.key === "ArrowLeft") {
                  rightRef.current.focus();
                  setFace("right");
                } else if (event.key === "ArrowRight") {
                  leftRef.current.focus();
                  setFace("left");
                }
              }}
            ></div>
            <div
              className={`col-start-2 col-span-1 row-start-3 row-span-1 border-2 border-black ${
                inputFace == "bottom" ? "bg-black animate-opacity-fade" : ""
              }`}
              onClick={() => {
                setFace("bottom");
              }}
              tabIndex={0}
              ref={bottomRef}
              onKeyDown={(event) => {
                if (event.key === "ArrowUp") {
                  frontRef.current.focus();
                  setFace("front");
                } else if (event.key === "ArrowDown") {
                  topRef.current.focus();
                  setFace("top");
                } else if (event.key === "ArrowLeft") {
                  leftRef.current.focus();
                  setFace("left");
                } else if (event.key === "ArrowRight") {
                  rightRef.current.focus();
                  setFace("right");
                }
              }}
            ></div>
          </div>
        </div>

        <div className="relative w-full h-[400px] my-2">
          <video
            ref={videoRef}
            className="w-full h-full object-cover transform scale-x-[-1]"
            autoPlay
            muted
          ></video>

          {/* Overlay with squares, arranged based on coordinates */}
          <div className="absolute inset-0 flex flex-col justify-center items-center pointer-events-none">
            {squares.map((square, index) => (
              <div
                key={index}
                className="absolute"
                style={{
                  left: `${square.x}px`,
                  top: `${square.y}px`,
                  width: `${square.size}px`,
                  height: `${square.size}px`,
                  border: "4px solid black",
                }}
              />
            ))}
          </div>
        </div>

        <div className="">
          <button
            onClick={() => {
              stopCamera();
              onClose();
            }}
            className="bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700 transition duration-300 w-full"
          >
            Stop
          </button>
        </div>

        {/* {results.length > 0 && (
          <div className="mt-4">
            <h3 className="text-black text-lg">Detected Colors:</h3>
            <ul>
              {results.map((result, index) => (
                <li key={index}>
                  Color: {result.color}, Position:{" "}
                  {JSON.stringify(result.position)}
                </li>
              ))}
            </ul>
          </div>
        )} */}
      </div>
    </div>
  );
};

export default CameraPopup;
