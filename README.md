# Projet Generateur de formes geometriques Flask + Next.js

Ce projet est une application web utilisant **Flask** pour le backend (API REST) et **Next.js** pour le frontend (interface utilisateur reactive).  
Il sert de base pour developper des applications modernes avec une separation claire entre le client et le serveur.

## Structure du projet

.
├── client/generateur/                    
│   ├── .next/                 
│   ├── app/                  
│   ├── components/           
│   ├── lib/                   
│   ├── public/                
│   ├── node_modules/          
│   ├── .gitignore             
│   ├── components.json        
│   ├── eslint.config.mjs      
│   ├── next.config.ts         
│   ├── next-env.d.ts          
│   ├── package.json           
│   ├── package-lock.json      
│   ├── postcss.config.mjs     
│   ├── README.md              
│   ├── tsconfig.json         
│
├── server/                    
│   ├── __pycache__/           
│   ├── .venv/               
│   ├── generateur.py          
│   ├── generateur_fractale...
│   ├── requirements.txt       
│   ├── server.py             
│
├── .gitignore               
├── README.md               

---

## Prérequis

- **Python 3.10+**
- **Node.js 18+** (npm ou yarn)
- **Git**
- **GhostScript** : -pour windows Telecharge l’installeur ici : https://www.ghostscript.com/download.html. Et ajoute le chemin d’installation a la variable d’environnement PATH.
                    -pour linux (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install ghostscript
```


---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Siksss/generateur.git
cd ton-projet
```

### 2. Lancer le backend

```bash
cd server
python -m venv .venv
source .venv\Scripts\activate       # ou .venv/bin/activate sur Linux
pip install -r requirements.txt
python server.py                # ou flask run si configure
```

### 3. Lancer le frontend

```bash
cd ../client/generateur
npm install
npm run dev
```

## Communication entre frontend et backend

Le frontend(http://localhost:3000) effectue des appels API vers http://localhost:5000.

## Auteur 

Developpe par Matias SOTTI-BAGARRE