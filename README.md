# Discord bot
A simple Discord server bot written in Python.

Create a Discord bot account: Go to the Discord Developer Portal and create a new application. Once you have created the application, go to the "Bot" section and click "Add Bot". Give your bot a name and avatar, and copy the bot token.

Set up your development environment: To develop the bot, you'll need a programming language and a Discord library. For this example, we'll be using Python and the discord.py library. You'll need to have Python and pip installed on your computer. To install discord.py, run the following command in your terminal: pip install discord.py.

Run your code: Save the file and run it in your terminal by typing python your_bot_file.py. 

In your Discord applications go to your bot > OAuth2 > URL Generator > select scopes and permissions it needs to function ie scope: 'bot' permission: 'send messages' > take the generated URL and paste it to your Discord channel or channel you want to activate the bot in, important: if it is not your server you will need the server owners permission to be activated!

If everything is working properly, you should see your bot come online in your Discord server.

Test bot: Go to your Discord server and send a message starting with !hello or whatever command you have included in your code. Your bot should respond with "Hello!".
