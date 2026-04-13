# Report Setmanal de Visites — Dashboard

Dashboard web per visualitzar els reports setmanals de visites comercials.

## Estructura del projecte

```
report-dashboard/
├── index.html      # Aplicació web (tot en un sol fitxer)
├── data.json       # Dades del report (generades des de l'Excel)
└── README.md       # Aquest fitxer
```

## Com publicar a GitHub Pages

### 1. Crea un repositori a GitHub

Ves a [github.com/new](https://github.com/new) i crea un nou repositori, per exemple `report-visites`.

### 2. Puja els fitxers

Des del teu ordinador, obre un terminal i executa:

```bash
cd report-dashboard
git init
git add .
git commit -m "Afegir dashboard de visites"
git branch -M main
git remote add origin https://github.com/EL-TEU-USUARI/report-visites.git
git push -u origin main
```

### 3. Activa GitHub Pages

1. Ves al teu repositori a GitHub
2. Clica **Settings** (configuració)
3. Al menú esquerre, clica **Pages**
4. A **Source**, selecciona `Deploy from a branch`
5. A **Branch**, selecciona `main` i la carpeta `/root (root)`
6. Clica **Save**

Al cap d'uns minuts, la web estarà disponible a:
```
https://EL-TEU-USUARI.github.io/report-visites/
```

## Com actualitzar les dades

Quan tinguis un nou report setmanal (Excel), cal regenerar el `data.json`.
Pots fer-ho amb aquest script Python:

```bash
pip install openpyxl pandas
python3 actualitzar_dades.py NOU_REPORT.xlsx
```

I després pujar el nou `data.json` al repositori:

```bash
git add data.json
git commit -m "Actualitzar dades setmana XX"
git push
```

La web s'actualitzarà automàticament.
