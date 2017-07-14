import girder_client
import json
import os
import pprint
import sys
import time

if len(sys.argv) < 3:
    print('USAGE: upload_and_process.py PATH_TO_FILE PARENT_FOLDER_ID')
    sys.exit(1)

# TODO substitute your girder URL and API key. Make sure API key
# has data read, data write, and task execute scope.
client = girder_client.GirderClient(apiUrl='http://34.229.214.79/api/v1')
client.authenticate(apiKey='sLrP2DWBEUCZWnc5FiWT4I2WufA9AaFuRQm8bi1j')

path = sys.argv[1]
folderId = sys.argv[2]
itemTaskId = '59654b114d2d8d4d6eaa0f0f'  # TODO substitute your own item task ID
print('Creating item')
item = client.createItem(parentFolderId=folderId, name=os.path.basename(path))
print('Uploading file')
file = client.uploadFileToItem(item['_id'], path)
print('Launching offline processing')
job = client.post('item_task/%s/execution' % itemTaskId, parameters={
    'inputs': json.dumps({
        'InputImage': {
            'mode': 'girder',
            'resource_type': 'item',
            'id': item['_id']
        },
        'Threshold': {'mode': 'inline', 'data': 200},
        'ClosingRadius': {'mode':'inline', 'data': 2}
    }),
    'outputs': json.dumps({
        'SegmentedImage': {
            'mode': 'girder',
            'parent_id': folderId,
            'parent_type': 'folder',
            'name': 'output_%d_%s' % (int(time.time()), item['name'])
        }
    })
})
print('Job was created:')
pprint.pprint(job)



