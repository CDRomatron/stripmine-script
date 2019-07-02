from sadfaceparser.sadfaceparser import Sadfaceparser
import uuid
import datetime
import json
import os


def openfile(dir, id):
    with open(os.getcwd() + dir + 'output_' + id + '/OUTPUT.json') as f:
        return json.load(f)


def setuptemplate():
    return dict(
        analyst_email="",
        analyst_name="",
        created=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        edges=[],
        edited="",
        id=str(uuid.uuid4()),
        metadata={},
        nodes=[],
        resources=[]
    )


def filltemplate(template, data):
    for s in data['document']:
        if 'evidence' in s:
            template['nodes'].append(
                {"id": str(uuid.uuid4()), "metadata": {"type": 'evidence'}, "text": s['evidence'], "type": "atom"})
        if 'claim' in s:
            template['nodes'].append(
                {"id": str(uuid.uuid4()), "metadata": {"type": 'claim'}, "text": s['claim'], "type": "atom"})
        if 'claim_evidence' in s:
            template['nodes'].append(
                {"id": str(uuid.uuid4()), "metadata": {"type": 'claim_evidence'}, "text": s['claim_evidence'],
                 "type": "atom"})


class Margotsadfaceparser(Sadfaceparser):
    directory = ''

    def __init__(self, dir):
        self.directory = dir

    def tosadface(self, id):
        sadface = setuptemplate()
        filltemplate(sadface, openfile(self.directory, id))
        return sadface
