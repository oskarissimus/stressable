import httpx
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from stressable.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_instant():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/instant")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


@pytest.mark.asyncio
async def test_wait():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/wait")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


@pytest.mark.asyncio
async def test_wait_random():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/wait-random")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}
