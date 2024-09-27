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

  const analyzeFrame = async () => {
    if (videoRef.current) {
      const canvas = document.createElement("canvas");
      canvas.width = videoRef.current.videoWidth;
      canvas.height = videoRef.current.videoHeight;
      const context = canvas.getContext("2d");
      context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

      const imageDataUrl = canvas.toDataURL("image/png").split(",")[1];

      const response = await fetch("http://127.0.0.1:5000/scan", {
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
        <video
          ref={videoRef}
          className="w-full h-[400px] bg-white"
          autoPlay
          muted
        ></video>
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
