from fastapi import FastAPI

from routers.guest import router as guest_router
from routers.chain import router as chain_router
from routers.branch import router as branch_router
from routers.reservation import router as reservation_router
from routers.conversation import router as conversation_router
from routers.message import router as message_router
from routers.faq import router as faq_router
from routers.policy import router as policy_router
from routers.knowledge_document import router as knowledge_document_router
from routers.feedback import router as feedback_router
from routers.support_ticket import router as support_ticket_router
from routers.cancellation_request import router as cancellation_request_router
from routers.chat import router as chat_router

app = FastAPI(
    title="Hotel Chatbot API",
    version="1.0.0",
    debug=True
)

app.include_router(guest_router)
app.include_router(chain_router)
app.include_router(branch_router)
app.include_router(reservation_router)
app.include_router(conversation_router)
app.include_router(message_router)
app.include_router(faq_router)
app.include_router(policy_router)
app.include_router(knowledge_document_router)
app.include_router(feedback_router)
app.include_router(support_ticket_router)
app.include_router(cancellation_request_router)

# AI Chat Router
app.include_router(chat_router)