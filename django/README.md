#### Este repositorio será para demonstração do conteudo de curso em um appweb encapsulando com iframes todos os dashboards gerados pela equipe nas ferramentas externas como Google Data Studio, PowerBI ou outros...

Como instalar depois de clonar o repositorio

~~~python
#Criar o virtual enviroment com o comando abaixo
python -m venv venv
#carregar o novo virtual enviroment
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser 
python manage.py changepassword

python manage.py runserver 
~~~


Sequencia de códigos utilizara para criar ambiente inteiro. 
(não ha mais necessidade de repetir o abaixo)

~~~python
(venv) $ django-admin startproject proj .
(venv) $ django-admin startapp app1 

~~~
GitBash
source venv/Scripts/Activate

Editar o arquivo app1\urls.py
Editar o arquivo app1\views.py
Editar o arquivo app1\dashboard?.py
Editar o arquivo app1\base.py