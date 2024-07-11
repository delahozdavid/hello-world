from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class DialogflowWebhookRequest(BaseModel):
    queryResult: dict
    
@app.post('/webhook')
async def webhook(request: Request):
    request_data = await request.json()
    webhook_request = DialogflowWebhookRequest(**request_data)
    intent_name = webhook_request.queryResult['intent']['displayName']
    print(intent_name)
    
    
    if intent_name == 'curp_found':
        
        return {"FulfillmentText": "Repuesta de mi Webhook"}
    
    return {"Fulfillment": "Intent no manejado"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)