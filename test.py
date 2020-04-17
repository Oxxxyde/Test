from pyrogram import Client

# Create a new Client instance
api_id = "1208098"
api_hash = "31449da46f94afaaa6c632f3ca9a4c36"

app = Client("my_account", api_id, api_hash)


with app:
    # Send a message, Markdown is enabled by default
    app.send_message("me", "Hi there! I'm using **Pyrogram**")

app.run()