from girder.utility.model_importer import ModelImporter
from girder.api import access
from girder.api.describe import autoDescribeRoute, Description
from girder.api.rest import filtermodel, getCurrentUser
from girder import events
from girder.constants import AccessType


@access.public
@filtermodel('item')
@autoDescribeRoute(
    Description('List all items that need to be processed')
    .pagingParams(defaultSort='name')
)
def _getToBeProcessed(limit, offset, sort, params):
    itemModel = ModelImporter.model('item')
    cursor = itemModel.find({
        'meta.toBeProcessed': { '$eq': True }
    }, sort=sort)
    return list(itemModel.filterResultsByPermission(
        cursor, user=getCurrentUser(), limit=limit, offset=offset, level=AccessType.READ))


def _onUpload(event):
    file = event.info['file']
    if 'itemId' in file:
        itemModel = ModelImporter.model('item')
        item = itemModel.load(file['itemId'], force=True)
        itemModel.setMetadata(item, {'toBeProcessed': True})


def load(info):
    ModelImporter.model('item').ensureIndex(['meta.toBeProcessed', {'sparse': True}])

    events.bind('model.file.finalizeUpload.after', info['name'], _onUpload)

    info['apiRoot'].item.route('GET', ('to_be_processed',), _getToBeProcessed)
