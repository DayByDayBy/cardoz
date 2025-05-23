import React, { useEffect, useRef, useState } from 'react';

//  hook for background pattern 
const useBackgroundPattern = ({
  stringToRepeat = "1234567890",
  fontSize = 16,
  lightMode = false
}) => {
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const runningRef = useRef(true);
  const charPositionsRef = useRef([]);

  const drawBase = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = `${fontSize}px monospace`;
    ctx.fillStyle = lightMode ? "rgba(0, 0, 0, 0.4)" : "rgba(255, 255, 255, 0.4)";

    charPositionsRef.current = [];

    const charWidth = ctx.measureText("0").width;
    const lineHeight = fontSize + 4;
    const charsPerLine = Math.ceil(canvas.width / charWidth);
    const lines = Math.ceil(canvas.height / lineHeight);

    let index = 0;
    for (let y = 0; y < lines; y++) {
      for (let x = 0; x < charsPerLine; x++) {
        const char = stringToRepeat[index % stringToRepeat.length];
        const posX = x * charWidth;
        const posY = y * lineHeight + fontSize;

        ctx.fillText(char, posX, posY);
        charPositionsRef.current.push({ char, x: posX, y: posY });
        index++;
      }
    }
  };

  const animateHighlightGroup = () => {
    if (!runningRef.current) return;

    const charPositions = charPositionsRef.current;
    const groupCount = Math.floor(charPositions.length / 4);
    const groupIndex = Math.floor(Math.random() * groupCount);
    const start = groupIndex * 4;
    const group = charPositions.slice(start, start + 4);

    const duration = 1000;
    const fadeIn = 350, visible = 300, fadeOut = 350;
    let startTime = performance.now();

    const animate = (time) => {
      const canvas = canvasRef.current;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      const elapsed = time - startTime;

      let alpha = 0;
      if (elapsed < fadeIn) {
        alpha = elapsed / fadeIn;
      } else if (elapsed < fadeIn + visible) {
        alpha = 1;
      } else if (elapsed < duration) {
        alpha = 1 - ((elapsed - fadeIn - visible) / fadeOut);
      } else {
        drawBase();
        animationRef.current = requestAnimationFrame(animateHighlightGroup);
        return;
      }

      ctx.font = `${fontSize}px monospace`;
      const base = lightMode ? 0.2 : 0.2;
      const final = lightMode ? 1 : 0;
      const fill = lightMode
        ? `rgba(255, 255, 255, ${base + alpha * (1 - base)})`
        : `rgba(0, 0, 0, ${base + alpha * 0.6})`;

      ctx.fillStyle = fill;
      group.forEach(({ char, x, y }) => {
        ctx.fillText(char, x, y);
      });

      animationRef.current = requestAnimationFrame(animate);
    };

    animationRef.current = requestAnimationFrame(animate);
  };

  const start = () => {
    runningRef.current = true;
    drawBase();
    animateHighlightGroup();
  };

  const stop = () => {
    runningRef.current = false;
    if (animationRef.current) {
      cancelAnimationFrame(animationRef.current);
    }
  };

  return {
    canvasRef,
    start,
    stop,
    drawBase
  };
};

// Background Pattern Component
const BackgroundPattern = ({
  stringToRepeat = "1234567890",
  fontSize = 10,
  lightMode = false
}) => {
  const { canvasRef, start, stop, drawBase } = useBackgroundPattern({
    stringToRepeat,
    fontSize,
    lightMode
  });

  useEffect(() => {
    const handleResize = () => drawBase();
    window.addEventListener('resize', handleResize);
    
    start();

    return () => {
      window.removeEventListener('resize', handleResize);
      stop();
    };
  }, [stringToRepeat, fontSize, lightMode]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        zIndex: -1,
        pointerEvents: 'none'
      }}
    />
  );
};

// Main App Component
const App = () => {
  const [stringToRepeat, setStringToRepeat] = useState("1234567890");
  const [lightMode, setLightMode] = useState(false);

  return (
    <div style={{
      margin: 0,
      padding: 0,
      height: '100vh',
      background: '#111',
      fontFamily: '"Courier New", monospace',
      overflow: 'hidden',
      position: 'relative'
    }}>
      <BackgroundPattern 
        stringToRepeat={stringToRepeat}
        fontSize={10}
        lightMode={lightMode}
      />
      
      <div style={{
        position: 'relative',
        zIndex: 1,
        padding: '20px',
        color: 'white',
        fontSize: '16px'
      }}>
        <p>etcetc</p>
        
        <div style={{ marginTop: '20px' }}>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ display: 'block', marginBottom: '5px' }}>
              Background String:
            </label>
            <input
              type="text"
              value={stringToRepeat}
              onChange={(e) => setStringToRepeat(e.target.value)}
              style={{
                padding: '5px',
                fontSize: '14px',
                background: '#333',
                color: 'white',
                border: '1px solid #555',
                borderRadius: '3px'
              }}
            />
          </div>
          
          <button
            onClick={() => setLightMode(!lightMode)}
            style={{
              padding: '8px 16px',
              fontSize: '14px',
              background: '#0c863d',
              color: 'white',
              border: 'none',
              borderRadius: '3px',
              cursor: 'pointer'
            }}
          >
            Toggle {lightMode ? 'Dark' : 'Light'} Mode
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;