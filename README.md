# DND remote music

## What'a fuck?

This application for playing selected in server audio file on clients computers

## Starting

### Linux

#### Getting requirments

##### Debian/Ubuntu

```
sudo apt-get install python
sudo apt-get install ffmpeg
```

##### Arch/Manjaro

```
sudo pacman -S python
sudo pacman -S ffmpeg
```

#### Setup

```
git clone https://github.com/viv3000/dndRemoteMusic
python -m pip install --upgrade pip
python -m pip install playsound
cd dndRemoteMusic/
```

#### Settings

1. Add your music in 'music/' folder
2. Update settings.py

#### Run

##### Server

```
python server.py
```

##### Client

```
python client.py
```

### Windows

#### Getting requirments

1. Install git from [site](https://git-scm.com/download/win)
2. Install python from [site](https://www.python.org/downloads)
3. Install vlc from [site](https://www.videolan.org/vlc/download-windows.ru.html)

#### Setup

```
git clone https://github.com/viv3000/dndRemoteMusic
python -m pip install --upgrade pip
pip install playsound
cd dndRemoteMusic/
```

#### Settings

1. Add your music in 'music/' folder
2. Update settings.py

#### Run

##### Server

```
suckDick.exe
```

##### Client

```
python client.py
```

