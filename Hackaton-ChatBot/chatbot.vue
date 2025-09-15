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
                  <img src="data:image/png;base64,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" alt="Logo Pine" />
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
