<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col
        cols="12"
        sm="10"
        md="8"
        lg="6"
        xl="4"
      >    
      <v-card :style="{ backgroundColor: backgroundColor, width: '100%' }" class="chat-card">
          <v-card-title :style="{ backgroundColor: primaryColor, color: backgroundColor }" class="headline">
            Banco Pine Chatbot
          </v-card-title>
          <!-- Chat Messages -->
          <v-divider></v-divider>
          <v-card-text>
            <div class="chat-window">
              <div
                v-for="(message, index) in messages"
                :key="index"
                :class="['chat-bubble', message.sender]"
              >
                <!-- Avatar for bot -->
                <div v-if="message.sender === 'bot'" class="chat-bubble-avatar">
                  <img src="data:image/png;base64" alt="Logo Pine" />
                </div>
                <!-- Avatar spacer for user messages -->
                <div v-else-if="message.sender === 'user'" class="chat-bubble-avatar-spacer"></div>

                <!-- Message content -->
                <div class="chat-bubble-content">
                  {{ message.text }}
                </div>

                <!-- Buttons for options -->
                <div v-if="message.sender === 'options'" class="button-container">
                  <button
                    v-for="(option, idx) in message.options"
                    :key="idx"
                    @click="handleOptionSelection(option)"
                  >
                    {{ option }}
                  </button>
                </div>
              </div>
            </div>
          </v-card-text>
          <!-- Input Field -->
          <v-divider></v-divider>
          <v-card-actions :style="{ backgroundColor: primaryColor }">
            <v-text-field
              :style="{ backgroundColor: backgroundColor }"
              v-model="userInput"
              label="Digite sua mensagem"
              @keyup.enter="sendMessage"
              clearable
              hide-details
              outlined
              dense
              full-width
            ></v-text-field>
            <v-btn @click="sendMessage" :style="{ backgroundColor: secondaryColor, color: backgroundColor }">Enviar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      userInput: '',
      primaryColor: '#71242B',
      secondaryColor: '#b0a080', // White color
      backgroundColor: '#ffffff',
      accountId: 123,
    };
  },
  methods: {
      async sendMessage() {
          if (this.userInput.trim() === '') return;
          this.addMessage(this.userInput, 'user');
          const userMessage = this.userInput;
          this.userInput = '';
          await this.getBotResponse(userMessage);
      },
      addMessage(text, sender) {
          this.messages.push({ text, sender });
      },
      async getBotResponse(userInput) {
          try {
              const response = await axios.post(
                  'http://localhost:5271/api/ai/chat',
                  { message: userInput },
                  {
                      headers: {
                          'Content-Type': 'application/json',
                      },
                  }
              );
              const botReply = response.data.response;
              this.addMessage(botReply, 'bot');
          } catch (error) {
              console.error(error);
              this.addMessage('Desculpe, ocorreu um erro ao processar sua solicitação. Front-end', 'bot');
          }
      },
  }
};
</script>


<style scoped>
.chat-window {
  flex-grow: 1; /* Faz a janela de chat crescer para ocupar o espaço restante */
  overflow-y: auto; /* Habilita a rolagem quando necessário */
  padding-right: 10px;
  height: auto; /* Remove qualquer restrição de altura */
}
.text-left {
  display: flex;
  justify-content: flex-start;
}
.text-right {
  display: flex;
  justify-content: flex-end;
}
.option-button {
  margin: 5px 5px 0 0;
  color: #ffffff;
}
.quote-card {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 8px;
  margin: 10px 0;
}
.currency-image {
  width: 50px;
  height: 50px;
}
.quote-info {
  text-align: center;
  font-size: 12px;
  color: #666;
}

/* Responsive adjustments */
@media (min-width: 600px) {
  .chat-window {
    height: 60vh;
  }
}

@media (min-width: 960px) {
  .chat-window {
    height: 70vh;
  }
}

/* Input Row Styles */
.input-row {
  display: flex;
  align-items: stretch;
  background-color: #fdf0d7;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 10px;
  width: 100%;
}

textarea {
  flex-grow: 1;
  margin: 0 10px;
}

.input-row button {
  background-color: #f0e6fb;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  color: #00000089;
  box-shadow: 1px 2px 3px rgba(0, 0, 0, 0.25);
  transition: background-color 0.2s ease-in-out, box-shadow 0.1s ease-in-out;
}

button:hover {
  filter: brightness(0.9);
}

button:active {
  box-shadow: none;
}

.input-row .btn-clear {
  background-color: #f17b7b;
}

/* Chat Bubble Styles */
.chat-bubble {
  display: flex;
  align-items: center;
  flex-direction: row;
  margin-bottom: 10px;
}

.chat-bubble.user {
  flex-direction: row-reverse;
}

.chat-bubble.bot {
  flex-direction: row;
}

.chat-bubble-avatar {
  flex-shrink: 0;
  background-color: #e1e1e1;
  border-radius: 50%;
  height: 40px;
  width: 40px;
  margin: 0px 10px;
  overflow: hidden;
}

.chat-bubble-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.chat-bubble-avatar-spacer {
  width: 60px; /* Adjust to match avatar width */
}

.chat-bubble-content {
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  max-width: 80%;
}

.user .chat-bubble-content {
  background-color:rgba(113, 36, 42, 0.73);
  color: #ffffff;
}

.bot .chat-bubble-content {
  background-color:rgba(113, 36, 42, 0.93);
  color: #ffffff;
}

/* Styles for Buttons in Options */
.button-container {
  margin-top: 10px;
}

.button-container button {
  background-color: #f0e6fb;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  color: #00000089;
  box-shadow: 1px 2px 3px rgba(0, 0, 0, 0.25);
  transition: background-color 0.2s ease-in-out, box-shadow 0.1s ease-in-out;
  margin-right: 5px;
}

.button-container button:hover {
  filter: brightness(0.9);
}

.button-container button:active {
  box-shadow: none;
}
</style>
