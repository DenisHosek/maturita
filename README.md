![build status](../../actions/workflows/build.yml/badge.svg) ![coverage](./coverage.svg)

# maturita
# Aplikace pro výpočet úročení

## Úvod

Tento repozitář obsahuje formulář, databázi a výpočet na jednoduché a složené úročení. Mým cílem bylo poskytnout tento výpočet v co nejvíce praktickém a moderním prostředí. 

## Funkcionalita

Aplikace nabízí následující funkce:

- Výpočet jednoduchého a složeného úročení, tento výpočet umožní uživateli vypočítat úrok.
- Parktickým a moderním prostředí se snaží co nejvíce zpříjemnit používání.
- Zobrazení výpočtů přihlášeného uživatele.
- Přihlášení a registraci

## Technologie

Aplikace je vyvinuta s využitím moderních technologií:

- *Frontend:* HTML, CSS, Bootstrap a Javascript
- *Backend:* Python - Django
- *Databáze:* MariaDB

## Instalace

Pro spuštění a instalaci aplikace postupujte podle následujících kroků:

1. Nainstalujte docker: https://www.docker.com/

2. Naklonujte repozitář do vašeho lokálního stroje:

   Díky HTTPS:
   
     git clone https://github.com/DenisHosek/maturita.git

   nebo skrze SSH protocol:
     git clone git@github.com:DenisHosek/maturita.git

   Dle Vaší preference.

4. Přejděte do složky s projektem přes příkazovou řádku:

   cd maturita

5. Použijte příkaz *docker compose build* pro sestavení aplikace
   
6. Spusťte databázové migrace:
   
   *./run.sh migrate*

4. Spusťte Django server:

   *docker compose up*


Po spuštění serveru je aplikace dostupná na portu 8200.

## Použití

Po spuštění aplikace můžete přistoupit můžete vypočítat úroky dle Vaší potřeby.
