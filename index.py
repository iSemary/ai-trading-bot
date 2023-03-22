from classes.SendMessage import SendMessage
import json
# # Send Alert Message via telegram
# SendMessage("822482686", "HI").send()
# SendMessage("822482686", "HIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHI").sendQuestionButtons(['Sell', 'Buy'])

rawFile = open('rsi-strategy.ipynb').read()
cells = json.loads(rawFile)
cells = cells["cells"]

codeCells = []
for i in cells:
    if i["cell_type"] == "code":
        codeCells.append(i["source"])

cellDefinitionsRaw = open('rsi-strategy.json').read()
cellDefinitions = json.loads(cellDefinitionsRaw)