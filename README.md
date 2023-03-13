# DiscordServerCloner

<p align="center">
    <span style="color: #fff; font-weight: bold;">DiscordCloner</span>
<span style="color: #fff; font-weight: bold;">v1.0.0</span>

This program allows you to clone any discord server just using its ID

# Usage

1. Download executable file [here](https://www.mediafire.com/file/xrkv44nymwyc1dh/DiscordCloner.zip/file), after that unzip it.

- **IMPORTANT**: `config.json` and `main.exe` files have to be in same folder or else program will not work!

2. Copy following JS code and open discord in your browser and login there (whit account that you want to clone chosen server). Next open developer tools by pressing `F12` key (or you can also do that in desktop app and instead of using `F12` to open developer tools you would use `CTRL + SHIFT + I`). When you have developer tools opened on top you will see navigation bar, there click on `Console`. Now here in console paste JS code that you copied earlier. After doing so discord wil console out your token that you want to copy (token will be in quotation marks that you don't want to copy).

- **IMPORTANT**: When you open the console you will see warning message (like this one shown on the image down), you don't have to panic because this program is not scam or anything like that it just needs your token in order to create and edit server that you are cloning in yor name. Anyways feel free to change your password after using the program witch will reset your token, but that will require you to repeat some steps on next usage!

<p align="center">
  <img alt="issue" src="https://github.com/Josakko/DiscordServerCloner/blob/main/assets/image.png?raw=true" width="650px">
</p>

- **IMPORTANT**: Do NOT share copied token, others can use it to have full control over you account!

JS code that you have to paste in console:

    (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()

<p align="center">
 <span style="color: #fff; font-weight: bold;">OR</span>
</p>

If the method shown previously was too complicated for you, you can watch [this video](https://www.youtube.com/watch?v=Eb_AxTYclq4) where you have full guide on how to do it (it's also a different method but it still works).

3. Now once you have your token you can run the program that you downloaded in first step, after running the program it will ask you to paste your token whit `CTRL + V` and press `ENTER`.

4. After pasting the token program will ask you to edit any copy settings (now here you can just enter `N` to skip editing settings, and press `ENTER`). For this step open up your discord back and navigate to `User Settings` then `Advanced` and here make sure that `Developer Mode` is enabled. 

5. Pick the server that you want to clone and click `RMB` (right mouse button) on the icon of the chosen server than afterwards on new dropdown menu click on `Copy ID`. Next go back to the program and paste there copied ID. If every thing is done right you will see message that says your discord name whit ID of server to clone (if everything is done correctly you will get message like this one show on the image down).

<p align="center">
  <img alt="issue" src="https://github.com/Josakko/DiscordServerCloner/blob/main/assets/screenshot.png?raw=true" width="600px">
</p>

6. Just wait for program to finish cloning!

- **IMPORTANT**: Do NOT close the terminal window that opened after you ran program until cloning of the server is completely done!

## Need Help?

If you need help contact me on my [discord server](https://discord.gg/xgET5epJE6).

## Contributors

Big thanks to all of the amazing people (only me) who have helped by contributing to this project!
