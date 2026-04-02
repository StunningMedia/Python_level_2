from tkinter import messagebox

# hier een lijst van berichten die we dadelijk gaan gebruiken
grappige_berichten = [
    "Dit programma heeft besloten om je dag op te vrolijken in plaats van je bestanden te versleutelen. Goed gedaan, programma!",
    "Geen zorgen, dit is gewoon een virtueel knuffelvirus. Je computer wordt nu overspoeld met digitale knuffels!",
    "Gefeliciteerd! Je hebt de enige nutteloze virusmelding ter wereld ontvangen. Wees trots op jezelf!",
    "Dit 'virus' heeft je computer bekeken en besloten dat het een beetje stoffig is. Tijd om te stofzuigen!",
    "Waarschuwing: dit virus heeft je computer geïnfecteerd met positiviteit en goede vibes. Wees alert op glimlachen!"
]

# loop over alle berichten ....
for bericht in grappige_berichten:
    # ...    en toon elk bericht in een messageBox
    messagebox.showinfo("Virus", bericht)