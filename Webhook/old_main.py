from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

class PaymentEvent(BaseModel):
    amount: float
    description: str
    webhook_url: str

def send_webhook(payload: dict):
    try:
        requests.post('', json=payload)
    except requests.exceptions.RequestException as e:
        print(e)


@app.post('/payment')
def payment_event(payment_event: PaymentEvent, background_task: BackgroundTasks):
    if not payment_event.amount:
        raise HTTPException(status_code=400, detail="Amount can't be blank")
    background_task.add_task(send_webhook, {
        "amount": payment_event.amount,
        "description": payment_event.description,
        "webhook_url": payment_event.webhook_url
    })
    return {
        "status": 200,
        "data" : payment_event.__dict__
    }
    
    @app.post('/webhook')
    async def receive_webhook_event(request: Request):
        data = await request.json()
        return {
            "message": 'webhook received'
        }
        
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)