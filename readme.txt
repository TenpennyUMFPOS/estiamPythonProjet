# Retro reels center

Retro Réels Center vise à fournir une plateforme permettant aux clients de louer des films à partir d'un catalogue diversifié. Il gère les données des clients, les informations sur les films et les enregistrements de location, permettant aux clients de parcourir et de louer des films tout en conservant un historique des locations..

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Features

- Opérations CRUD pour trois applications dans le projet : films, customers, rentalrecords.
- Obtenez le nombre de films loués par un client spécifique.
- Obtenez une liste de films dans un genre spécifique.

## Usage 

- Exécutez "python manage.py runserver" dans le terminal.  

## API Documentation
- Pour accéder à la documentation de l'API, exécutez d'abord le serveur, puis ouvrez ce lien dans votre navigateur et ajoutez '/docs/' à la fin de l'URL ou.
- List des endpoint : 
	- /customers/ 
	- /films/
	-rentals/ : Dans Create Utilisez cet exemple :
 		  	 		   {
					    "customer":"/customers/2/",
					    "film":"/films/3/",
					    "rentaldate":"2023-09-10",
					    "returndate":"2023-09-17"
   				     	    }
	-/customer-movies-rented/<int:customer_id>/
	-/movies-by-genre/<str:genre>/ 

## Testing 
- Pour tester, exécutez cette commande dans le terminal "python manage.py test nomdduapp.tests"


