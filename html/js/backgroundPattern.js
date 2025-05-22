export function createBackgroundPattern({
  target = document.body,
  stringToRepeat = "1234567890",
  fontSize = 16,
  lightMode = false
} = {}) {
  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");

  canvas.style.position = "fixed";
  canvas.style.top = "0";
  canvas.style.left = "0";
  canvas.style.zIndex = "-1";
  canvas.style.pointerEvents = "none";

  target.appendChild(canvas);

  let charPositions = [];
  let running = true;

  function drawBase() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = `${fontSize}px monospace`;
    ctx.fillStyle = lightMode ? "rgba(0, 0, 0, 0.4)" : "rgba(255, 255, 255, 0.4)";

    charPositions = [];

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
        charPositions.push({ char, x: posX, y: posY });
        index++;
      }
    }
  }

  function animateHighlightGroup() {
    if (!running) return;

    const groupCount = Math.floor(charPositions.length / 4);
    const groupIndex = Math.floor(Math.random() * groupCount);
    const start = groupIndex * 4;
    const group = charPositions.slice(start, start + 4);

    const duration = 1000;
    const fadeIn = 350, visible = 300, fadeOut = 350;
    let startTime = performance.now();

    function animate(time) {
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
        return requestAnimationFrame(animateHighlightGroup);
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

      requestAnimationFrame(animate);
    }

    requestAnimationFrame(animate);
  }

  function start() {
    running = true;
    drawBase();
    animateHighlightGroup();
  }

  function stop() {
    running = false;
  }

  function updateString(newString) {
    stringToRepeat = newString;
    drawBase();
  }

  function toggleMode() {
    lightMode = !lightMode;
    drawBase();
  }

  window.addEventListener("resize", drawBase);

  start();

  return {
    updateString,
    toggleMode,
    stop,
    start,
  };
}
