from sadfaceparser.sadfaceparser import Sadfaceparser
import uuid
import datetime

def setuptemplate():
    core = dict(
        analyst_email="",
        analyst_name="",
        created=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        description="",
        edited="",
        id=str(uuid.uuid4()),
        notes="",
        title="",
        version=""
    )

    metadata = dict(
        core=core
    )

    base = dict(
        edges=[],
        metadata=metadata,
        nodes=[],
        resources=[]
    )

    return base


def filltemplate(template, data, meta):
    template['metadata']['extended'] = meta
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

    def tosadface(self, jsonin, meta):
        sadface = setuptemplate()
        filltemplate(sadface, jsonin, meta)
        return sadface
