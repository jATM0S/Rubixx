import React, { useRef, useEffect, useState } from "react";

const CameraPopup = ({ onClose }) => {
  const videoRef = useRef(null);
  const mediaStreamRef = useRef(null);
  const [results, setResults] = useState([]);

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        mediaStreamRef.current = stream;
        videoRef.current.play();
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
    { x: 150, y: 100, size: 60 }, 
    { x: 250, y: 100, size: 60 }, 
    { x: 350, y: 100, size: 60 }, 
    { x: 150, y: 200, size: 60 }, 
    { x: 250, y: 200, size: 60 }, 
    { x: 350, y: 200, size: 60 }, 
    { x: 150, y: 300, size: 60 }, 
    { x: 250, y: 300, size: 60 }, 
    { x: 350, y: 300, size: 60 }, 
  ];
  const analyzeFrame = async () => {
    if (videoRef.current) {
      const canvas = document.createElement("canvas");
      canvas.width = videoRef.current.videoWidth;
      canvas.height = videoRef.current.videoHeight;
      const context = canvas.getContext("2d");
      context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

      const croppedImages = squares.map(({ x, y, size }) => {
        const imageData = context.getImageData(x, y, size, size); // Crop square
        const cropCanvas = document.createElement("canvas"); // Create a new canvas for each crop
        cropCanvas.width = size;
        cropCanvas.height = size;
        const cropContext = cropCanvas.getContext("2d");
        cropContext.putImageData(imageData, 0, 0); // Paste the cropped image onto the new canvas
        return cropCanvas; // Return the cropped canvas
      });  

      const response = await fetch("http://127.0.0.1:8000/scan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ image: imageDataUrl }),  
      });

      const data = await response.json();
      setResults(data);
    }
  };

  useEffect(() => {
    startCamera();

    const intervalId = setInterval(analyzeFrame, 1000); // Analyze every second

    return () => {
      clearInterval(intervalId);
      stopCamera(); // Cleanup on component unmount
    };
  }, []);

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-75 z-50">
      <div className="bg-white p-4 rounded shadow-lg">
        <h2 className="text-black text-2xl mb-4">Camera Feed:</h2>
        <div className="relative w-full h-[400px]">
          <video
            ref={videoRef}
            className="w-full h-full object-cover transform scale-x-[-1] z-0"
            autoPlay
            muted
          ></video>

           {/* Overlay with squares, arranged based on coordinates */}
          <div className="absolute inset-0 flex flex-col justify-center items-center pointer-events-none z-10">
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
        <div className="mt-4">
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
        {results.length > 0 && (
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
        )}
      </div>
    </div>
  );
};

export default CameraPopup;
