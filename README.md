<h1 align="center">
Agenda de Contatos
</h1>

<h5 align="center">
    Um site de estudos com back-end feito em python, utilizando django.
</h5>

### Instalando python 3.8.x

• Linux

```console
sudo apt-get install python3.8 && sudo apt-get install python-pip
```

• MacOS

```console
brew install python3.8
```

• Windows

<a href="https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe">Downlaod x86</a>, <a href="https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe">Download x86-64</a>

### Criando e Ativando Ambiente Virtual

Para criar, na pasta raíz do projeto:

```console
virtualenv venv
```

Para ativá-lo:

• Windows

```console
venv\Scripts\activate
```

• Linux ou MacOS

```console
source venv/bin/activate
```

### Instalando dependencias

```console
pip install -r requirements.txt
```

ou

```console
pip3 install -r requirements.txt
```

### Iniciar servidor

```console
python manage.py runserver
```