aufgaben = [
    {
    "text": "python lernen",
    "erledigt": False
    },
    {
    "text": "Shake trinken",
    "erledigt": True
    }
]
def text(aufgb):
    return(aufgb["Text"])

def emoji(aufgb):
    if aufgb["erledigt"] == True:
            return("✅")
    else:
        return("❌")


for task in aufgaben:
    print(text(task) + emoji(task))