window.addEventListener("DOMContentLoaded", () => {
    const messages = document.createElement("ul");
    const message = document.createElement("img");
    document.body.appendChild(messages);
  
    const websocket = new WebSocket("ws://localhost:5765/");
    websocket.onmessage = ({ data }) => {
      const messagem = JSON.parse(data)
      message.setAttribute("src", `data:image/${messagem.type};base64,${messagem.url}`);
      messages.appendChild(message);
    };
  });