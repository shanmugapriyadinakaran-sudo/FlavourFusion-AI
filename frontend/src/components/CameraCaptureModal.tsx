import React, { useRef, useState, useEffect } from 'react';
import { Camera, RefreshCw, Check, X, AlertCircle } from 'lucide-react';

interface CameraCaptureModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCapture: (file: File) => void;
}

export const CameraCaptureModal: React.FC<CameraCaptureModalProps> = ({
  isOpen,
  onClose,
  onCapture,
}) => {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [stream, setStream] = useState<MediaStream | null>(null);
  const [capturedBlob, setCapturedBlob] = useState<Blob | null>(null);
  const [capturedPreview, setCapturedPreview] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (isOpen) {
      startCamera();
    } else {
      stopCamera();
    }
    return () => {
      stopCamera();
    };
  }, [isOpen]);

  const startCamera = async () => {
    setError(null);
    setCapturedBlob(null);
    setCapturedPreview(null);
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        throw new Error('Camera access is not supported by your browser.');
      }
      const mediaStream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment', width: { ideal: 1280 }, height: { ideal: 720 } },
        audio: false,
      });
      setStream(mediaStream);
      if (videoRef.current) {
        videoRef.current.srcObject = mediaStream;
      }
    } catch (err: any) {
      setError(err.message || 'Unable to access camera. Please allow camera permissions.');
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      setStream(null);
    }
  };

  const takePhoto = () => {
    if (!videoRef.current || !canvasRef.current) return;
    const video = videoRef.current;
    const canvas = canvasRef.current;
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob((blob) => {
      if (blob) {
        setCapturedBlob(blob);
        const url = URL.createObjectURL(blob);
        setCapturedPreview(url);
      }
    }, 'image/jpeg', 0.9);
  };

  const retakePhoto = () => {
    if (capturedPreview) {
      URL.revokeObjectURL(capturedPreview);
    }
    setCapturedBlob(null);
    setCapturedPreview(null);
  };

  const confirmPhoto = () => {
    if (!capturedBlob) return;
    const file = new File([capturedBlob], `ingredient_capture_${Date.now()}.jpg`, {
      type: 'image/jpeg',
    });
    onCapture(file);
    stopCamera();
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/80 backdrop-blur-sm">
      <div className="relative w-full max-w-lg bg-ivory-50 rounded-2xl shadow-2xl border border-ivory-300 overflow-hidden flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-ivory-200">
          <div className="flex items-center space-x-2 text-forest-700">
            <Camera className="w-5 h-5 text-sage-600" />
            <h3 className="font-semibold text-base">Ingredient Camera Capture</h3>
          </div>
          <button
            onClick={() => {
              stopCamera();
              onClose();
            }}
            className="p-1.5 rounded-lg text-stone-400 hover:text-stone-700 hover:bg-ivory-200 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Viewfinder / Preview */}
        <div className="relative aspect-video bg-black flex items-center justify-center overflow-hidden">
          {error ? (
            <div className="p-6 text-center text-ivory-100 max-w-sm">
              <AlertCircle className="w-10 h-10 text-terracotta-400 mx-auto mb-2" />
              <p className="text-sm font-medium">{error}</p>
              <button
                onClick={startCamera}
                className="mt-4 px-4 py-1.5 rounded-lg bg-forest-600 text-white text-xs font-semibold hover:bg-forest-500"
              >
                Retry Camera
              </button>
            </div>
          ) : capturedPreview ? (
            <img
              src={capturedPreview}
              alt="Captured Food Frame"
              className="w-full h-full object-cover"
            />
          ) : (
            <>
              <video
                ref={videoRef}
                autoPlay
                playsInline
                muted
                className="w-full h-full object-cover"
              />
              {/* Food capture reticle guide */}
              <div className="absolute inset-8 border-2 border-dashed border-white/40 rounded-xl pointer-events-none flex items-center justify-center">
                <span className="text-[11px] font-semibold text-white/80 bg-black/40 px-2.5 py-1 rounded-full backdrop-blur-sm">
                  Center food ingredients here
                </span>
              </div>
            </>
          )}
          <canvas ref={canvasRef} className="hidden" />
        </div>

        {/* Controls footer */}
        <div className="p-4 bg-ivory-100 flex items-center justify-between border-t border-ivory-200">
          {capturedBlob ? (
            <>
              <button
                onClick={retakePhoto}
                className="flex items-center space-x-1.5 px-4 py-2 rounded-xl text-stone-700 bg-ivory-200 hover:bg-ivory-300 text-sm font-medium transition-colors"
              >
                <RefreshCw className="w-4 h-4" />
                <span>Retake</span>
              </button>
              <button
                onClick={confirmPhoto}
                className="flex items-center space-x-1.5 px-5 py-2 rounded-xl bg-forest-600 text-white hover:bg-forest-500 text-sm font-semibold shadow-sm transition-colors"
              >
                <Check className="w-4 h-4" />
                <span>Analyze Captured Photo</span>
              </button>
            </>
          ) : (
            <>
              <span className="text-xs text-stone-500">Hold steady in good culinary lighting</span>
              <button
                onClick={takePhoto}
                disabled={!stream}
                className="flex items-center space-x-2 px-6 py-2.5 rounded-xl bg-terracotta-600 hover:bg-terracotta-500 text-white font-semibold text-sm shadow-md transition-all disabled:opacity-50"
              >
                <Camera className="w-4 h-4" />
                <span>Capture Photo</span>
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
