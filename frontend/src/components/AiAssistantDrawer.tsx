import React, { useState, useRef, useEffect } from 'react';
import {
  Sparkles,
  Send,
  X,
  ChefHat,
  Flame,
  ArrowRight,
  Bot,
  User as UserIcon,
  HelpCircle,
  Minimize2,
  Maximize2
} from 'lucide-react';
import { api } from '../services/api';
import { SuggestedPairingItem } from '../types';

interface AiAssistantDrawerProps {
  currentIngredients?: string[];
  onAddIngredients?: (ingredients: string[]) => void;
  isOpen: boolean;
  onToggle: () => void;
}

interface Message {
  sender: 'user' | 'assistant';
  text: string;
  vibe?: string;
  pairings?: SuggestedPairingItem[];
  timestamp: string;
}

export const AiAssistantDrawer: React.FC<AiAssistantDrawerProps> = ({
  currentIngredients = [],
  onAddIngredients,
  isOpen,
  onToggle
}) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      sender: 'assistant',
      text: "Yo foodie! 👋 I'm **Chef Fusion AI**, your flavor chemistry bestie. Wondering why soy sauce on vanilla ice cream tastes like salted caramel? 🍨 Need an unhinged midnight snack or curious what you can cook with your ingredients? Ask away!",
      vibe: 'Culinary Bestie 🔥',
      pairings: [
        {
          title: 'Unhinged Salted Caramel Sundae',
          ingredients: ['Vanilla', 'Soy Sauce'],
          tastes_like: 'Rich Salted Caramel & Toasted Toffee',
          reason: 'Umami glutamates suppress bitterness while vanillin explodes in perceived sweetness!'
        }
      ],
      timestamp: 'Just now'
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const quickPrompts = [
    '🍦 Why does Vanilla + Soy Sauce taste like caramel?',
    '🌙 Quick 5-min midnight snack idea',
    '🤯 Give me 3 unhinged pairings that slap',
    '🧪 What can I cook with ingredients in my Lab?'
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    if (isOpen) {
      scrollToBottom();
    }
  }, [messages, isOpen]);

  const handleSend = async (messageText?: string) => {
    const textToSend = messageText || input;
    if (!textToSend.trim() || loading) return;

    const userMsg: Message = {
      sender: 'user',
      text: textToSend.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!messageText) setInput('');
    setLoading(true);

    try {
      const res = await api.assistant.chat({
        message: textToSend,
        current_ingredients: currentIngredients
      });

      const assistantMsg: Message = {
        sender: 'assistant',
        text: res.reply,
        vibe: res.vibe || 'Flavor Alchemist ✨',
        pairings: res.suggested_pairings,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          sender: 'assistant',
          text: "My neural tastebuds got a bit overwhelmed, but I'm back! Try asking about sweet & savory flavor illusions.",
          vibe: 'Chef Error 🫠',
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {/* Floating Action Button */}
      {!isOpen && (
        <button
          onClick={onToggle}
          className="fixed bottom-6 right-6 z-40 flex items-center space-x-2.5 px-4 py-3 rounded-full bg-forest-600 dark:bg-forest-500 hover:bg-forest-500 text-white shadow-xl hover:shadow-2xl hover:scale-105 active:scale-95 transition-all duration-200 border-2 border-sage-300 dark:border-forest-400 group"
        >
          <div className="relative">
            <ChefHat className="w-5 h-5 text-sage-200 animate-bounce" />
            <span className="absolute -top-1 -right-1 flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-terracotta-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-terracotta-500"></span>
            </span>
          </div>
          <span className="font-semibold text-sm tracking-wide">Ask Chef AI</span>
          <span className="text-[11px] font-bold px-1.5 py-0.5 rounded-full bg-sage-700/60 text-sage-200 uppercase tracking-wider">
            AI Chef
          </span>
        </button>
      )}

      {/* Slide-out Drawer */}
      {isOpen && (
        <div className="fixed inset-y-0 right-0 z-50 w-full sm:w-[440px] bg-white dark:bg-[#141b18] border-l border-ivory-300 dark:border-forest-900 shadow-2xl flex flex-col transition-all duration-300 animate-in slide-in-from-right">
          {/* Header */}
          <div className="p-4 border-b border-ivory-200 dark:border-forest-900 bg-ivory-50/80 dark:bg-[#1a2320] flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-forest-600 dark:bg-forest-500 text-white flex items-center justify-center shadow-sm">
                <ChefHat className="w-6 h-6 text-sage-200" />
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <h3 className="font-bold text-stone-900 dark:text-ivory-100 text-base">
                    Chef Fusion AI
                  </h3>
                  <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-forest-100 dark:bg-forest-900 text-forest-700 dark:text-sage-300 border border-forest-200 dark:border-forest-700">
                    Online 🟢
                  </span>
                </div>
                <p className="text-xs text-stone-500 dark:text-stone-400">
                  Culinary Chemistry & Flavor Alchemy
                </p>
              </div>
            </div>

            <button
              onClick={onToggle}
              className="p-1.5 rounded-lg text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-ivory-200 dark:hover:bg-forest-900 transition-all"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Quick Prompts Bar */}
          <div className="px-4 py-2.5 bg-ivory-100 dark:bg-[#111714] border-b border-ivory-200 dark:border-forest-900/60 overflow-x-auto no-scrollbar flex space-x-2">
            {quickPrompts.map((prompt, i) => (
              <button
                key={i}
                onClick={() => handleSend(prompt)}
                disabled={loading}
                className="whitespace-nowrap px-3 py-1 rounded-full text-xs font-medium bg-white dark:bg-[#1e2723] hover:bg-sage-50 dark:hover:bg-forest-800 text-forest-700 dark:text-sage-300 border border-ivory-300 dark:border-forest-800 shadow-2xs transition-all active:scale-95"
              >
                {prompt}
              </button>
            ))}
          </div>

          {/* Message Stream */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.map((msg, idx) => (
              <div
                key={idx}
                className={`flex flex-col ${msg.sender === 'user' ? 'items-end' : 'items-start'}`}
              >
                <div className="flex items-center space-x-1.5 mb-1 text-[11px] text-stone-400 dark:text-stone-500">
                  {msg.sender === 'assistant' ? (
                    <>
                      <Sparkles className="w-3.5 h-3.5 text-forest-500" />
                      <span className="font-semibold text-forest-600 dark:text-sage-400">Chef AI</span>
                      {msg.vibe && (
                        <span className="px-1.5 py-0.2 rounded-full bg-terracotta-50 dark:bg-terracotta-900/40 text-terracotta-600 dark:text-terracotta-400 font-bold border border-terracotta-200 dark:border-terracotta-800 text-[10px]">
                          {msg.vibe}
                        </span>
                      )}
                    </>
                  ) : (
                    <>
                      <UserIcon className="w-3 h-3 text-stone-400" />
                      <span>You</span>
                    </>
                  )}
                  <span>• {msg.timestamp}</span>
                </div>

                <div
                  className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
                    msg.sender === 'user'
                      ? 'bg-forest-600 text-white rounded-tr-none shadow-sm'
                      : 'bg-ivory-100 dark:bg-[#1c2521] text-stone-800 dark:text-ivory-100 border border-ivory-200 dark:border-forest-900 rounded-tl-none shadow-2xs'
                  }`}
                >
                  <p className="whitespace-pre-line">{msg.text}</p>

                  {/* Suggested Pairings / Recipes */}
                  {msg.pairings && msg.pairings.length > 0 && (
                    <div className="mt-3 space-y-2 pt-2 border-t border-ivory-200 dark:border-forest-800">
                      <div className="text-[11px] font-bold uppercase tracking-wider text-stone-500 dark:text-stone-400 flex items-center space-x-1">
                        <Flame className="w-3.5 h-3.5 text-terracotta-500" />
                        <span>Suggested Culinary Formula</span>
                      </div>
                      {msg.pairings.map((p, pIdx) => (
                        <div
                          key={pIdx}
                          className="p-2.5 rounded-xl bg-white dark:bg-[#141b18] border border-sage-200 dark:border-forest-800 text-xs shadow-2xs"
                        >
                          <div className="font-bold text-forest-800 dark:text-sage-200 text-sm">
                            {p.title}
                          </div>
                          {p.tastes_like && (
                            <div className="mt-1 inline-flex items-center space-x-1 px-2 py-0.5 rounded-md bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 font-semibold text-[11px] border border-amber-200 dark:border-amber-800">
                              <span>✨ Tastes Like:</span>
                              <span>{p.tastes_like}</span>
                            </div>
                          )}
                          <div className="mt-1.5 flex flex-wrap gap-1">
                            {p.ingredients.map((ing, iIdx) => (
                              <span
                                key={iIdx}
                                className="px-1.5 py-0.5 rounded bg-ivory-200 dark:bg-forest-900 text-stone-700 dark:text-stone-300 text-[10px]"
                              >
                                {ing}
                              </span>
                            ))}
                          </div>
                          {p.reason && (
                            <p className="mt-1 text-[11px] text-stone-500 dark:text-stone-400">
                              {p.reason}
                            </p>
                          )}
                          {onAddIngredients && (
                            <button
                              onClick={() => onAddIngredients(p.ingredients)}
                              className="mt-2 w-full flex items-center justify-center space-x-1 py-1 px-2 rounded-lg bg-forest-50 dark:bg-forest-900/60 hover:bg-forest-100 dark:hover:bg-forest-800 text-forest-700 dark:text-sage-300 font-medium text-[11px] border border-forest-200 dark:border-forest-700 transition-all"
                            >
                              <span>Load into Flavor Lab 🧪</span>
                              <ArrowRight className="w-3 h-3" />
                            </button>
                          )}
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {loading && (
              <div className="flex items-center space-x-2 text-stone-400 dark:text-stone-500 text-xs italic">
                <ChefHat className="w-4 h-4 animate-spin text-forest-500" />
                <span>Chef AI is simmering the science...</span>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Box */}
          <div className="p-3 border-t border-ivory-200 dark:border-forest-900 bg-ivory-50/90 dark:bg-[#1a2320]">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSend();
              }}
              className="flex items-center space-x-2"
            >
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask about flavor illusions, recipes, snacks..."
                className="flex-1 px-4 py-2.5 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#121815] text-stone-800 dark:text-ivory-100 text-sm focus:outline-none focus:ring-2 focus:ring-forest-500 dark:focus:ring-forest-400 placeholder:text-stone-400"
              />
              <button
                type="submit"
                disabled={!input.trim() || loading}
                className="p-2.5 rounded-xl bg-forest-600 dark:bg-forest-500 hover:bg-forest-500 text-white disabled:opacity-40 disabled:cursor-not-allowed shadow-sm transition-all"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
          </div>
        </div>
      )}
    </>
  );
};
