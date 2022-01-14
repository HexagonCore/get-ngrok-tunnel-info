[![CodeFactor](https://www.codefactor.io/repository/github/hexagoncore/get-ngrok-tunnel-info/badge)](#/)
[<img src="https://img.shields.io/github/license/HexagonCore/get-ngrok-tunnel-info">](#/)
[<img src="https://img.shields.io/github/stars/HexagonCore/get-ngrok-tunnel-info">](#/)
[<img src="https://img.shields.io/github/forks/HexagonCore/get-ngrok-tunnel-info">](#/)
[<img src="https://img.shields.io/github/issues/HexagonCore/get-ngrok-tunnel-info">](#/)


# Get ngrok tunnel info
Easy and fast tool written in **python 3** to get info about running ngrok tunnel. Supports **HTTPS** and **TCP**
___
### ‎

## Instalation
* ### Windows / macOS
	Run `python3 -m pip install ngrok_info`
	
* ### Linux
	Run `python3 -m pip install ngrok_info`
### ‎

## Usage
* ### Windows / macOS / Linux
	Add this to your script: `import ngrok_info`<br/> ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎`ngrok_info.get()`
	 ‎
	
	Now, if you run it, you will see output with some **info**. If ngrok is not running on your computer, it will output error. After you run it, you can acess the info as variables too!
	
	If you are using **config file** to specify tunnel preset, use `ngrok_info.get("TUNNEL_NAME")` (Replace *TUNNEL_NAME* with your tunnel name. Please do not delete quotation marks.)

	If you do not want output, but **only variables**, use `ngrok_info.get_notext()`

	If tunnel is **TCP**, you have access these variables: `ngrok_info.tnl_name`, `ngrok_info.tnl_type`, `ngrok_info.adress`, `ngrok_info.ip` and `ngrok_info.port`.

	With **https** tunnel, you can acess these variables: `ngrok_info.tnl_name`, `ngrok_info.tnl_type`, `ngrok_info.adress` and `ngrok_info.ip`.
	

### ‎

## Uninstallation
* ### Windows / macOS
	Run `python3 -m pip uninstall ngrok-info`
	
* ### Linux
	Run `python3 -m pip uninstall ngrok-info`

### ‎
## FAQ
* ### Error: wrong tunnel name specified or no tunnel is running
	Check if ngrok is really running on your computer.
	If yes, check if you have correctly specified [tunnel name](https://ngrok.com/docs#tunnel-definitions). You need to specify it only, if you are using [config file](https://ngrok.com/docs#config-default-location) to specify tunnel preset. If you've checked everything, but it's still not working, contact [us on Discord](https://discord.gg/agREa6Dh3r) or [open issue](https://github.com/HexagonCore/get-ngrok-tunnel-info/issues/new/choose).
### ‎


Do you like this? Hit that ⭐!                                
Use the star button as way to show us, that it works              
Forks and pull requests are welcome of course
 
