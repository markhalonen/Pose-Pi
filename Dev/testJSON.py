import json
payload = '{"command":"snap","args":{"photo_event_id":"8caf3697-c327-40b2-a264-38be621cfa7d","hw_id":"8f2c1519-80a6-4209-8c4b-a3ca9aee40a1"}}'
payload = json.loads(payload)
print payload
print 'args' in payload
print 'hw_id' in payload["args"]