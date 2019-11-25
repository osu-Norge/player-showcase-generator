<h1>player-showcase-generator</h1>

A simple script that fetches user info and divides it up into separate `.txt` files. This helps automating the proscess of making player/team showcases in [OBS](https://github.com/obsproject/obs-studio)


This script was made for the **o!NT 2019** osu! tournament. This means that it was specifically made for 2v2 tournaments however it can easily be adapted to support other tournament formats.

<br>

![Script in use - GIF](https://i.imgur.com/sHzTKJp.gif)

<br>

<h2>Getting started</h2>

<h3>Prerequisites</h2>

* [Python](https://github.com/python/cpython) 3.6 or newer

<h3>Installing & Running</h3>

*Assming that you have set your Python 3 path to `python`.*

* Install the required Python modules:
  ```
  python -m pip install -r requirements.txt
  ```

<br>

* Rename the [config.yaml.example](config.yaml.example) file to `config.yaml` and insert/replace all the values listed in the file with your own.
    
    **Note**:
    * `Team1` consists of `Player0` & `Player1`. 
    * `Team2` consists of `Player2` & `Player3`.

<br>

* Run the [showcase_generator.py](showcase_generator.py) file
  ```
  python showcase_generator.py
  ```

<br>

<h2 align="center">License</h2>

MIT - see the [LICENSE.md](LICENSE.md) file for details.

##
<div align="center">
  <h3>Project developed by</h3>
  <a href="https://discord.gg/Y7zyjGU"><img src="https://raw.githubusercontent.com/osu-Norge/assets/master/banner.png"></a>
</div>