<h1 align="center">
Coreboard
<a href='./LICENSE'>
    <img alt='License' src='https://img.shields.io/badge/Licence-MIT-green.svg'/>
</a>
<a href='https://docs.python.org/3/'>
    <img alt='Python 3.4+' src='https://img.shields.io/badge/python-3.4+-blue.svg'/>
</a>
<img align='center' alt='coreboard-logo' width='250' src='./coreboard-logo.png'/>
</h1>

Coreboard, The Python-Flask framework for building web board applications

## Coreboard structure

```
application
├── application
│   ├── __init__.py
│   ├── database.py
│   ├── static
│   │   ├── README.md
│   │   ├── css
│   │   │   ├── board.css
│   │   │   ├── font-awesome.min.css
│   │   │   └── quill.snow.css
│   │   └── js
│   │       ├── quill.js
│   │       └── sha512.js
│   ├── templates
│   │   ├── board
│   │   │   ├── article.html
│   │   │   ├── view.html
│   │   │   └── write.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── mainpage.html
│   │   └── signup.html
│   └── views
│       ├── __init__.py
│       ├── auth.py
│       └── board.py
└── runserver.py
```

## Installation

### macOS

```
git clone https://github.com/JunhoYeo/coreboard.git
```

Clone this repository with `git`.

```
$ pip3 install -r requirements.txt
```

Install dependencies in `requirements.txt`.
