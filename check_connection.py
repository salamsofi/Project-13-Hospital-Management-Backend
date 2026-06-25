from app.db.database import engine

try:
    with engine.connect():
        print("Connected Successfully")

except Exception as e:
    print(e)