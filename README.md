<h1>player-showcase-generator</h1>

A simple script that fetches info about a set of osu! users and puts it into separate `.txt` files. The script aids the process of automating creation of team/player showcases in [OBS](https://github.com/obsproject/obs-studio).


This script was made specifically for the **o!NT 2019** osu! tournament. This means that it is written to support 2v2 tournaments. It can however be easily adapted to support other tournament formats if you have the know-how.

⚠️**This script makes 12 API requests & scrapes 8 images in the matter of a few seconds. Please do not run this script excessively**⚠️

<br>

![Script in use - GIF](https://i.imgur.com/ByQtA5O.gif)

<br>

<h2>Getting started</h2>

<h3>Prerequisites</h2>

* [Python](https://github.com/python/cpython) 3.6+

<h3>Installing & Running</h3>

*Assming that you have set your Python 3 path to `python`.*

* Install the required Python modules:
  ```
  python -m pip install -r requirements.txt
  ```

<br>

* Rename the [config.yaml.example](config.yaml.example) file to `config.yaml` and insert/replace all the values listed within it with your own.
    
    **Note**:
    * `Team1` consists of `Player0` & `Player1`. 
    * `Team2` consists of `Player2` & `Player3`.

<br>

* Run [showcase_generator.py](showcase_generator.py):
  ```
  python showcase_generator.py
  ```

<br>

<h2 align="center">License</h2>

MIT - Please read [LICENSE](LICENSE) for details.

##
<div align="center">
  <h3>Project developed by</h3>
  <a href="https://discord.gg/Y7zyjGU"><img src="https://raw.githubusercontent.com/osu-Norge/assets/master/banner.png"></a>
</div>
