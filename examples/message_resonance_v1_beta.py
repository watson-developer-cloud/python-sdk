import json
import watson_developer_cloud


message_resonance = watson_developer_cloud.MessageResonanceV1Beta()

print(json.dumps(message_resonance.datasets(), indent=2))

print(json.dumps(message_resonance.resonance('cpu processor chip', 1), indent=2))
