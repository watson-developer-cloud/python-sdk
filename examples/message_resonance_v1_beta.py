import json
from watson_developer_cloud import MessageResonanceV1Beta as MessageResonance


message_resonance = MessageResonance(username='YOUR SERVICE USERNAME',
                                     password='YOUR SERVICE PASSWORD')

print(json.dumps(message_resonance.datasets(), indent=2))

print(json.dumps(message_resonance.resonance('cpu processor chip', 1), indent=2))
