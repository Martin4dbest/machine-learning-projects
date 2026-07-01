const nameInput = document.getElementById("name");
const personalitySelect = document.getElementById("personality");
const customPrompt = document.getElementById("customPrompt");

const startBtn = document.getElementById("startBtn");
const sendBtn = document.getElementById("sendBtn");

const messageInput = document.getElementById("message");
const chatBox = document.getElementById("chatBox");
const status = document.getElementById("status");

let started = false;

// ===============================
// Show Custom Prompt
// ===============================

personalitySelect.addEventListener("change", () => {

    if (personalitySelect.value === "26") {

        customPrompt.style.display = "block";

    } else {

        customPrompt.style.display = "none";

    }

});


// ===============================
// Add Message
// ===============================

function addMessage(sender, text) {

    const div = document.createElement("div");

    div.classList.add("message");

    if (sender === "user") {

        div.classList.add("user");

    } else {

        div.classList.add("bot");

    }

    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}


// ===============================
// Start Chat
// ===============================

startBtn.addEventListener("click", async () => {

    const name = nameInput.value.trim();

    if (!name) {

        alert("Enter your name.");

        return;

    }

    const response = await fetch("/start_chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            name: name,

            personality: personalitySelect.value,

            custom_prompt: customPrompt.value

        })

    });

    const data = await response.json();

    if (data.success) {

        started = true;

        status.innerHTML = "Active Personality: <b>" + data.personality + "</b>";

        chatBox.innerHTML = "";

        addMessage(
            "bot",
            "Hello " + name + "! 👋\nHow can I help you today?"
        );

    }

});


// ===============================
// Send Message
// ===============================

async function sendMessage() {

    if (!started) {

        alert("Start the chat first.");

        return;

    }

    const message = messageInput.value.trim();

    if (message === "") return;

    addMessage("user", message);

    messageInput.value = "";

    addMessage("bot", "MartAI is typing...");

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            name: nameInput.value,

            message: message

        })

    });

    const data = await response.json();

    chatBox.removeChild(chatBox.lastChild);

    addMessage("bot", data.reply);

}


// ===============================
// Button Click
// ===============================

sendBtn.addEventListener("click", sendMessage);


// ===============================
// Press Enter
// ===============================

messageInput.addEventListener("keypress", function(e){

    if(e.key === "Enter"){

        sendMessage();

    }

});