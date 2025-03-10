from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from loguru import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request details
        request_body = await request.body()
        logger.info(f"Incoming Request: {request.method} {request.url}")
        logger.info(f"Request Body: {request_body.decode('utf-8') if request_body else 'No Body'}")

        # Process request and capture response
        response = await call_next(request)
        response_body = b""

        async for chunk in response.body_iterator:
            response_body += chunk

        # Log response details
        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response_body.decode('utf-8') if response_body else 'No Body'}")

        # Return response
        return Response(
            content=response_body, 
            status_code=response.status_code, 
            headers=dict(response.headers), 
            media_type=response.media_type)