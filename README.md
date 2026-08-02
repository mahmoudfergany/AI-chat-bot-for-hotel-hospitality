# 🏨 AI Hotel Assistant

> An AI-powered hotel assistant that helps guests receive fast, natural, and accurate responses about hotel services, reservations, FAQs, and policies.

---

## 📖 Overview

AI Hotel Assistant is an intelligent customer support system designed for the hospitality industry.

Instead of waiting for reception or searching through hotel information, guests can simply ask questions in natural language and receive instant, helpful responses.

The project combines a modern backend architecture with Large Language Models (LLMs) to create a scalable AI assistant capable of supporting hotel customers.

---

## ✨ Features

- 🤖 AI-powered conversational assistant
- 🏨 Hotel information assistant
- 📅 Reservation management
- ❓ Frequently Asked Questions (FAQs)
- 📜 Hotel policy assistance
- 💬 Conversation management
- 📝 Customer feedback management
- 🎫 Support ticket system
- 🚫 Reservation cancellation requests
- 🔄 Multi-provider AI architecture (Gemini-ready, easily extendable to OpenAI, Claude, Grok, OpenRouter)

---

## 🎯 Project Goal

The main objective of this project is to improve the hotel guest experience by providing:

- Instant responses
- 24/7 availability
- Reduced workload for reception staff
- Natural AI conversations
- Easy access to hotel information

---

## 🏗️ System Architecture

```text
                    Client
                       │
                       ▼
                FastAPI Backend
                       │
                       ▼
                 Chat Service
                       │
                       ▼
              Provider Factory
                       │
          ┌────────────┴────────────┐
          │
    Gemini Provider
          │
          ▼
      Google Gemini API

                 PostgreSQL
                       ▲
         Reservations • Policies
         FAQs • Messages • Guests
```

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- SQLModel
- PostgreSQL
- Alembic

### AI

- Google Gemini
- LangChain *(In Progress)*

### Database

- PostgreSQL

### Documentation

- Swagger UI / OpenAPI

---

## 📂 Project Structure

```text
app/
│
├── crud/
├── models/
├── routers/
├── schemas/
├── services/
├── providers/
├── database.py
├── main.py
└── ...
```

---

## 📊 Database Entities

- Guest
- Reservation
- Branch
- Conversation
- Message
- FAQ
- Policy
- Knowledge Document
- Feedback
- Support Ticket
- Cancellation Request

---

## 🤖 AI Workflow

```text
User

↓

Chat Endpoint

↓

Chat Service

↓

Provider Factory

↓

Gemini Provider

↓

Google Gemini

↓

AI Response
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Hotel-Assistant.git
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=...

GEMINI_API_KEY=YOUR_API_KEY

DEFAULT_PROVIDER=gemini

GEMINI_MODEL=gemini-3.5-flash-lite
```

---

### Run the server

```bash
uvicorn main:app --reload
```

---

## 📸 Screenshots

### Swagger API

(Add Screenshot)

---

### Chat Example

(Add Screenshot)

---

## 🔮 Future Improvements

- LangChain Agent
- AI Tools
- Conversation Memory
- OpenAI Support
- Claude Support
- Grok Support
- OpenRouter Support
- Authentication (JWT)
- Docker Deployment

---

## 👥 Team

- Mahmoud Fergany
- Basil Sherif
- Seif Elden
- Jana Hossam

---

## 🙏 Acknowledgments

Special thanks to:

- ACT Company
- Our Team Leaders
- Our Managers
- Everyone who supported us throughout the internship.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
