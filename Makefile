prod:
	sudo apt update
	sudo apt upgrade

	#python3.8 and pip3
	sudo apt install -y python3-pip

	#django
	sudo pip install Django==4.0.6


	#postgres
	sudo apt install postgresql postgresql-contrib

    #git
	cd /home
	sudo git clone https://github.com/kochnev/events.git
	cd events

	#uwsgi
	sudo pip install uwsgi
	sudo uwsgi --ini uwsgi/uwsgi.ini

	#nginx
	sudo apt install -y nginx
	sudo cp nginx/nginx_events.conf /etc/nginx/sites-available/
	sudo ln -s /etc/nginx/sites-available/nginx_events.conf /etc/nginx/sites-enabled/
	nginx

	#init django project
	sudo python manage.py collectstatic --noinput
	python manage.py makemigrations
	python manage.py migrate

