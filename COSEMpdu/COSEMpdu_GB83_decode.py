from asn1.codecs.ber import *
from collections import namedtuple
from COSEMpdu.COSEMpdu_GB83_member import *

membership = namedtuple('member', 'name type object')

acse_apdu_tag_to_member = {
    0: membership('aarq', Class.APPLICATION | Encoding.CONSTRUCTED, AARQ),
    1: membership('aare', Class.APPLICATION | Encoding.CONSTRUCTED, AARE),
    2: membership('rlrq', Class.APPLICATION | Encoding.CONSTRUCTED, RLRQ),
    3: membership('rlre', Class.APPLICATION | Encoding.CONSTRUCTED, RLRE)
}

xdlms_apdu_tag_to_member = {
    1: membership('initiateRequest', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, InitiateRequest),
    5: membership('readRequest', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, ReadRequest),
    6: membership('writeRequest', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, WriteRequest),
    8: membership('initiateResponse', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, InitiateResponse),
    12: membership('readResponse', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, ReadResponse),
    13: membership('writeResponse', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, WriteResponse),
    14: membership('confirmedServiceError', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, ConfirmedServiceError),
    15: membership('data-notification', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, DataNotification),
    22: membership('unconfirmedWriteRequest', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, UnconfirmedWriteRequest),
    24: membership('informationReportRequest', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, InformationReportRequest),
    33: membership('glo-initiateRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloInitiateRequest),
    37: membership('glo-readRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloReadRequest),
    38: membership('glo-writeRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloWriteRequest),
    40: membership('glo-initiateResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloInitiateResponse),
    44: membership('glo-readResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloReadResponse),
    45: membership('glo-writeResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloWriteResponse),
    46: membership('glo-confirmedServiceError', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloConfirmedServiceError),
    54: membership('glo-unconfirmedWriteRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloUnconfirmedWriteRequest),
    56: membership('glo-informationReportRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloInformationReportRequest),
    65: membership('ded-initiateRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedInitiateRequest),
    69: membership('ded-readRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedReadRequest),
    70: membership('ded-writeRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedWriteRequest),
    72: membership('ded-initiateResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedInitiateResponse),
    76: membership('ded-readResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedReadResponse),
    77: membership('ded-writeResponse', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedReadResponse),
    78: membership('ded-confirmedServiceError', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedConfirmedServiceError),
    86: membership('ded-unconfirmedWriteRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedUnconfirmedWriteRequest),
    88: membership('ded-informationReportRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedInformationReportRequest),
    192: membership('get-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GetRequest),
    193: membership('set-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, SetRequest),
    194: membership('event-notification-request', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, EventNotificationRequest),
    195: membership('action-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, ActionRequest),
    196: membership('get-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GetResponse),
    197: membership('set-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, SetResponse),
    199: membership('action-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, ActionResponse),
    200: membership('glo-get-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloGetRequest),
    201: membership('glo-set-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloSetRequest),
    202: membership('glo-event-notification-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloEventNotificationRequest),
    203: membership('glo-action-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloActionRequest),
    204: membership('glo-get-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloGetResponse),
    205: membership('glo-set-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloSetResponse),
    207: membership('glo-action-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, GloActionResponse),
    208: membership('ded-get-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedGetRequest),
    209: membership('ded-set-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedSetRequest),
    210: membership('ded-event-notification-request', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedEventNotificationRequest),
    211: membership('ded-actionRequest', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedActionRequest),
    212: membership('ded-get-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedGetResponse),
    213: membership('ded-set-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedSetResponse),
    215: membership('ded-action-response', Class.CONTEXT_SPECIFIC | Encoding.PRIMITIVE, DedActionResponse),
    216: membership('exception-response', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, ExceptionResponse),
    217: membership('access-request', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, AccessRequest),
    218: membership('access-response', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, AccessResponse),
    219: membership('general-glo-ciphering', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, GeneralGloCiphering),
    220: membership('general-ded-ciphering', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, GeneralDedCiphering),
    221: membership('general-ciphering', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, GeneralCiphering),
    223: membership('general-signing', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, GeneralSigning),
    224: membership('general-block-transfer', Class.CONTEXT_SPECIFIC | Encoding.CONSTRUCTED, GeneralBlockTransfer),
}


def COSEMpdu_decode(data, offset=0):
    if isinstance(data, str) is True:
        frame = bytearray.fromhex(data).hex()
    else:
        frame = bytearray(data)

    # application
    for tag in acse_apdu_tag_to_member.keys():
        if frame[offset] == encode_tag(tag, acse_apdu_tag_to_member[tag].type):
            return acse_apdu_tag_to_member[tag].object(data)

    # context_specific
    for tag in xdlms_apdu_tag_to_member.keys():
        if frame[offset] == encode_tag(tag, xdlms_apdu_tag_to_member[tag].type):
            return xdlms_apdu_tag_to_member[tag].object(data)


