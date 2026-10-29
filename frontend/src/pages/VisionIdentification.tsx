import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Camera,
  Upload,
  Sparkles,
  Check,
  AlertCircle,
  RefreshCw,
  Plus,
  ArrowRight,
  Info,
  ShieldCheck,
  Image as ImageIcon
} from 'lucide-react';
import { api } from '../services/api';
import { VisionIdentifyResponse, VisionCandidate } from '../types';
import { CameraCaptureModal } from '../components/CameraCaptureModal';

interface VisionIdentificationProps {
  onAddIngredientToLab: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const VisionIdentification: React.FC<VisionIdentificationProps> = ({ onAddIngredientToLab }) => {
  const navigate = useNavigate();
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [identifying, setIdentifying] = useState(false);
  const [result, setResult] = useState<VisionIdentifyResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Checkbox confirmation of detected candidates
  const [confirmedMap, setConfirmedMap] = useState<Record<string, boolean>>({});
  const [showCameraModal, setShowCameraModal] = useState(false);

  const handleFileSelect = (file: File) => {
    setError(null);
    setResult(null);
    setSelectedFile(file);
    const url = URL.createObjectURL(file);
    setImagePreview(url);
    processImage(file);
  };

  const processImage = async (file: File) => {
    setIdentifying(true);
    setError(null);
    try {
      const data = await api.vision.identify(file);
      setResult(data);
      // Default select candidates with confidence >= 60%
      const initialMap: Record<string, boolean> = {};
      data.candidates.forEach((c) => {
        initialMap[c.ingredient_name] = c.confidence >= 50;
      });
      setConfirmedMap(initialMap);
    } catch (err: any) {
      setError(err.message || 'Error identifying ingredients from image');
    } finally {
      setIdentifying(false);
    }
  };

  const toggleCandidate = (name: string) => {
    setConfirmedMap((prev) => ({
      ...prev,
      [name]: !prev[name],
    }));
  };

  const handleAddConfirmedToLab = () => {
    const confirmed = Object.entries(confirmedMap)
      .filter(([_, isChecked]) => isChecked)
      .map(([name]) => name);

    if (confirmed.length === 0) return;

    confirmed.forEach((name) => {
      onAddIngredientToLab(name, 100, 'g', 'Raw');
    });

    navigate('/lab');
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Header */}
      <div className="text-center max-w-2xl mx-auto space-y-3">
        <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-sage-100 dark:bg-forest-900/60 text-forest-700 dark:text-sage-300 text-xs font-semibold border border-sage-200 dark:border-forest-800">
          <Camera className="w-3.5 h-3.5" />
          <span>Computer Vision Food Intelligence</span>
        </div>
        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
          Identify Ingredients From Photos
        </h1>
        <p className="text-sm text-stone-600 dark:text-stone-300">
          Upload an ingredient photo or snap a snapshot directly with your camera. Our real computer vision model analyzes chromatic hues and surface gradients to suggest candidate ingredients.
        </p>
      </div>

      {/* Upload & Camera Actions Dropzone */}
      <div className="bg-ivory-50 dark:bg-[#151c19] rounded-3xl p-6 sm:p-10 border-2 border-dashed border-ivory-300 dark:border-forest-800 hover:border-forest-500 transition-colors shadow-sm text-center">
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => {
            if (e.target.files && e.target.files[0]) {
              handleFileSelect(e.target.files[0]);
            }
          }}
        />

        {imagePreview ? (
          <div className="max-w-md mx-auto space-y-4">
            <div className="relative aspect-video rounded-2xl overflow-hidden shadow-md border border-ivory-300 dark:border-forest-800">
              <img
                src={imagePreview}
                alt="Selected Food Preview"
                className="w-full h-full object-cover"
              />
              {identifying && (
                <div className="absolute inset-0 bg-stone-900/60 backdrop-blur-sm flex flex-col items-center justify-center text-ivory-50 space-y-2">
                  <RefreshCw className="w-8 h-8 animate-spin text-sage-300" />
                  <span className="text-xs font-semibold tracking-wide">
                    Extracting spectral color & edge features...
                  </span>
                </div>
              )}
            </div>

            <div className="flex items-center justify-center space-x-3">
              <button
                onClick={() => fileInputRef.current?.click()}
                className="px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900/60 hover:bg-ivory-300 dark:hover:bg-forest-800 text-stone-800 dark:text-ivory-100 text-xs font-semibold transition-colors"
              >
                Choose Different Photo
              </button>
              <button
                onClick={() => setShowCameraModal(true)}
                className="px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900/60 hover:bg-ivory-300 dark:hover:bg-forest-800 text-stone-800 dark:text-ivory-100 text-xs font-semibold transition-colors"
              >
                Retake with Camera
              </button>
            </div>
          </div>
        ) : (
          <div className="max-w-md mx-auto space-y-4">
            <div className="w-16 h-16 rounded-2xl bg-forest-600/10 dark:bg-forest-900 text-forest-700 dark:text-sage-300 flex items-center justify-center mx-auto">
              <ImageIcon className="w-8 h-8 text-forest-600 dark:text-sage-400" />
            </div>
            <div>
              <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">
                Drag and drop your food photo here
              </h3>
              <p className="text-xs text-stone-500 dark:text-stone-400 mt-1">
                Supports JPEG, PNG, and WEBP formats up to 10MB.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
              <button
                onClick={() => fileInputRef.current?.click()}
                className="w-full sm:w-auto flex items-center justify-center space-x-2 px-5 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-xs shadow-sm transition-all"
              >
                <Upload className="w-4 h-4" />
                <span>Upload From Device</span>
              </button>
              <button
                onClick={() => setShowCameraModal(true)}
                className="w-full sm:w-auto flex items-center justify-center space-x-2 px-5 py-2.5 rounded-xl bg-white dark:bg-[#1b2420] hover:bg-ivory-100 dark:hover:bg-forest-900 text-stone-800 dark:text-ivory-100 font-semibold text-xs border border-ivory-300 dark:border-forest-800 shadow-sm transition-all"
              >
                <Camera className="w-4 h-4 text-terracotta-600 dark:text-terracotta-400" />
                <span>Open Live Camera</span>
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Error notification */}
      {error && (
        <div className="p-4 rounded-2xl bg-terracotta-50 dark:bg-terracotta-950/40 border border-terracotta-200 dark:border-terracotta-800 text-terracotta-800 dark:text-terracotta-200 text-xs flex items-center space-x-3">
          <AlertCircle className="w-4 h-4 text-terracotta-600 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Identification Results Section */}
      {result && (
        <div className="bg-white dark:bg-[#151c19] rounded-3xl p-6 sm:p-8 border border-ivory-300 dark:border-forest-900 shadow-sm space-y-6 animate-fade-in">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-ivory-200 dark:border-forest-900 pb-4">
            <div>
              <span className="text-[11px] font-bold uppercase tracking-wider text-sage-600 dark:text-sage-400">
                Provider: {result.provider_used}
              </span>
              <h3 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50 mt-0.5">
                Candidate Detections ({result.candidates.length})
              </h3>
            </div>
            <p className="text-xs text-stone-500 dark:text-stone-400 max-w-sm sm:text-right">
              {result.message}
            </p>
          </div>

          {result.candidates.length === 0 ? (
            <div className="text-center py-10 space-y-2">
              <Info className="w-8 h-8 text-stone-400 mx-auto" />
              <p className="text-sm font-semibold text-stone-800 dark:text-ivory-100">No recognizable ingredients found</p>
              <p className="text-xs text-stone-500 dark:text-stone-400 max-w-md mx-auto">
                The image may be blurry or dimly lit. You can always search and add ingredients manually in the Flavor Lab.
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              <p className="text-xs text-stone-600 dark:text-stone-300 font-medium">
                Review and check the candidate ingredients you wish to add to your Flavor Lab workspace:
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {result.candidates.map((cand) => {
                  const isConfirmed = !!confirmedMap[cand.ingredient_name];
                  return (
                    <div
                      key={cand.ingredient_name}
                      onClick={() => toggleCandidate(cand.ingredient_name)}
                      className={`p-4 rounded-2xl border cursor-pointer transition-all flex items-start justify-between ${
                        isConfirmed
                          ? 'bg-forest-50/60 dark:bg-forest-900/40 border-forest-500 shadow-sm'
                          : 'bg-ivory-50 dark:bg-[#1b2420] border-ivory-300 dark:border-forest-800 opacity-70 hover:opacity-100'
                      }`}
                    >
                      <div className="space-y-1.5">
                        <div className="flex items-center space-x-2">
                          <span className="font-semibold text-stone-900 dark:text-ivory-100 text-sm">
                            {cand.ingredient_name}
                          </span>
                          <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-forest-600 text-white">
                            {cand.confidence}%
                          </span>
                        </div>
                        <p className="text-xs text-stone-500 dark:text-stone-400">{cand.category}</p>

                        <div className="space-y-0.5 pt-1">
                          {cand.visual_cues.map((cue, i) => (
                            <p key={i} className="text-[11px] text-stone-600 dark:text-stone-300 flex items-center space-x-1">
                              <span className="w-1.5 h-1.5 rounded-full bg-sage-400 shrink-0" />
                              <span>{cue}</span>
                            </p>
                          ))}
                        </div>
                      </div>

                      <div className={`w-6 h-6 rounded-lg flex items-center justify-center border transition-all ${
                        isConfirmed
                          ? 'bg-forest-600 text-white border-forest-600'
                          : 'bg-white dark:bg-[#151c19] border-ivory-300 dark:border-forest-800 text-transparent'
                      }`}>
                        <Check className="w-4 h-4" />
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Action Button */}
              <div className="pt-4 border-t border-ivory-200 dark:border-forest-900 flex flex-col sm:flex-row items-center justify-between gap-3">
                <span className="text-xs text-stone-500 dark:text-stone-400">
                  {Object.values(confirmedMap).filter(Boolean).length} ingredient(s) confirmed
                </span>
                <button
                  onClick={handleAddConfirmedToLab}
                  disabled={Object.values(confirmedMap).filter(Boolean).length === 0}
                  className="w-full sm:w-auto flex items-center justify-center space-x-2 px-6 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-xs shadow-md transition-all disabled:opacity-50"
                >
                  <Plus className="w-4 h-4" />
                  <span>Send Confirmed Ingredients to Flavor Lab</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Camera Capture Modal */}
      <CameraCaptureModal
        isOpen={showCameraModal}
        onClose={() => setShowCameraModal(false)}
        onCapture={(file) => handleFileSelect(file)}
      />
    </div>
  );
};
