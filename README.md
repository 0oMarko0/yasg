![pygame](pygame.png "Logo Title Text 1")

## YET ᗩᑎOTᕼEᖇ ᔕᑎᗩKE GᗩᗰE
This project as started during christmas time while i was off from school.
My main goal was to carry out a simple project while keeping as much as
i can a clean architecture. I just had done my architecture class
and i thought it would be a great way of appling what i have learned.

## ᗰOTIᐯᗩTIOᑎ
There's propablly more than enought snake game on github and on the web, so why 
chosing this ? The scale for this project was perfect for the time line i had to complete 
it. I've tried to focuse mainly on architecure. The main goal was to make this project as 
extensible as possible. I wanted the game logic completly independent from pygame so i could,
 if i want, make a web interface and a api whit [flask](http://flask.pocoo.org/) 
 
## IᑎᔕTᗩᒪᒪᗩTIOᑎ
#### Mac
You'll need to have brew install on your mac in order to follow those instruction.
Let's install python3.
```
brew install python3
```

Validate that we are using the good version (3.7.0)
```
python --version
```
If [pip](https://pypi.org/project/pip/) isn't install, go ahead and install it.
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Then
```
python get-pip.py
```

It's good pratice to install your python library in a virtual environment. 
That encapsulated your project so the library you install doesn't interfer with other python project you may have on your computer.
For this why are going to use [Virtualenv](https://virtualenv.pypa.io/en/latest/).

To install Virtualenv
```
pip install virtualenv
```

Once virtualenv is install we need to creat our environment. Go to the root of the project and type.
```
virtualenv venv
```

To active our environment
```
source venv/bin/activate
```

Finally we need to install the dependencies
```
pip install -r requirements.txt
```

Before lunching the program it's important to set the PYTHONPATH variable. This is necessary in order to tell python
 where to look for module.
 
 ```
export PYTHONPATH="$PWD"
```

To lunch the yasg, be sure to be in your virtualenv and at the root of the project.
```
python UI/main.py
```
 
## ᖴEᗩTᑌᖇEᔕ
#### Customisable Theme
The project include a theme generator that take a json as input. I've toke the json format found on [terminal.sexy](https://terminal.sexy/)

## ᑕOᗪE ᔕTYᒪE

## ᔕᑕᖇEEᑎᔕᕼOTᔕ

## ᖴᖇᗩᗰEᗯOᖇK ᑌᔕEᗪ
<b>Built with</b>
- [Python 3.7.0](https://www.python.org/downloads/release/python-370/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Pygame 1.9.4](https://www.pygame.org/news)

## ᑕOᑎTᖇIᗷᑌTE
Feel free to fork this repo and tweak this project as you wish