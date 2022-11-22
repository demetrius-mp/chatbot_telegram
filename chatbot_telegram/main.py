from create_app import create_app

app = create_app()

print("Bot started!")
app.run_polling()
