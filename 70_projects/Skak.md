# Projekt Skakbot

Kopier denne fil til dit eget Pycharm-projekt.  

## Projektmål

Programmer en skak-bot og en skak-engine, og opret den på lichess.org, så folk kan spille mod din bot på denne platform.

## Kom i gang

Foreløbig fungerer det kun med Python 3.12, men endnu ikke med Python 3.13!

I Pycharm, klik på File og Project from Version Control og clone https://github.com/lichess-bot-devs/lichess-bot.git

Læs repositorys ReadMe:

1\. Install lichess-bot

- Ignorer dette afsnit.

2\. Create a lichess OAuth token

- Der findes en fil config.yml.default i den repository, du clonede.
- Omdøb den til config.yml og brug den.

3\. Setup the engine

- Ignorer dette afsnit.

4\. Configure lichess-bot

- I config.yml under engine sæt protocol til "homemade" og name til ”RandomMove”.
- Ignorer resten af dette afsnit for nu.

5\. Upgrade to a BOT account

- Åbn et terminal vindue (Alt+F12)
- Udfør python lichess-bot.py -u (python, ikke python3, som står i dokumentationen)

6\. Run lichess-bot

- Ignorer dette afsnit.
- I stedet for åbn lichess_bot.py i pycharm og udfør den.

## Fremgangsmåde

Gå ikke bare i gang med at programmere, men lav en plan for, hvordan du vil gribe opgaven an.

Hvilke delmål/delprojekter findes?

Diskuter din plan med din lærer, før du begynder at kode.

## Ressourcer

### Hvordan fungerer forbindelsen mellem botten og lichess.org?

- Blog artikel: https://lichess.org/@/thibault/blog/how-to-create-a-lichess-bot/FuKyvDuB
- Lichess API dokumentation: https://lichess.org/api
- Afsnit om botter i denne dokumentation: https://lichess.org/api#tag/Bot

### Generelt om skakbot-algoritmer:

- Google fx ”chess bot algorithm”, “minimax algorithm”, “alpha-beta pruning”.
- Spørg Perplexity og lignende.

## Lad din bot spille mod andre botter

Mens din bot kører, udfør denne Python kode:  
(Tilpas `API_TOKEN` og `BOT_USERNAME`.)

```python
import requests

API_TOKEN = 'yourAPItoken'   # your API Token
BOT_USERNAME = 'maia1'       # the name of the other bot

url = f'https://lichess.org/api/challenge/{BOT_USERNAME}'
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'clock.limit': 300,      # 5 minutes
    'clock.increment': 0,    # 0 seconds increment
    'variant': 'standard',   # standard chess
    'rated': 'false'         # not rated
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.json())
```