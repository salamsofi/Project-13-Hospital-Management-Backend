from app.core.redis import redis_client

redis_client.set(
    "name",
    "Salam"
)

print(
    redis_client.get(
        "name"
    )
)