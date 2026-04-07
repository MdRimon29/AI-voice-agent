import os
from livekit import api
from dotenv import load_dotenv

load_dotenv()

token = (
    api.AccessToken(
        os.getenv("LIVEKIT_API_KEY"),
        os.getenv("LIVEKIT_API_SECRET"),
    )
    .with_identity("cli-user")
    .with_name("CLI User")
    .with_grants(
        api.VideoGrants(
            room_join=True,
            room="test-room",
        )
    )
)

print(token.to_jwt())