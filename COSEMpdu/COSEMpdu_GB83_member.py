from COSEMpdu.COSEMpdu_GB83 import *


class COSEMpduMember:
    member = None
    frame = None
    name = None

    def __init__(self, data):
        if isinstance(data, dict) is True:
            self.member = data
            self._encode_asn()
        else:
            if isinstance(data, str) is True:
                data = bytearray.fromhex(data)
            self.frame = data
            self._decode_asn()

    def _encode_asn(self):
        pass

    def _decode_asn(self):
        pass


"""
ACSE-APDU ::= CHOICE 
{     
    aarq                               AARQ-apdu,     
    aare                               AARE-apdu, 
    rlrq                               RLRQ-apdu,          -- OPTIONAL     
    rlre                               RLRE-apdu           -- OPTIONAL 
}
"""


class AARQ(COSEMpduMember):
    """
    AARQ-apdu ::= [APPLICATION 0] IMPLICIT SEQUENCE {
    -- [APPLICATION 0] == [ 60H ] = [ 96 ]

        protocol-version                   [0] IMPLICIT        BIT STRING {version1 (0)}    DEFAULT{version1},
        application-context-name           [1]                 Application-context-name,
        called-AP-title                    [2]                 AP-title OPTIONAL,
        called-AE-qualifier                [3]                 AE-qualifier OPTIONAL,
        called-AP-invocation-id            [4]                 AP-invocation-identifier OPTIONAL,
        called-AE-invocation-id            [5]                 AE-invocation-identifier OPTIONAL,
        calling-AP-title                   [6]                 AP-title OPTIONAL,
        calling-AE-qualifier               [7]                 AE-qualifier OPTIONAL,
        calling-AP-invocation-id           [8]                 AP-invocation-identifier OPTIONAL,
        calling-AE-invocation-id           [9]                 AE-invocation-identifier OPTIONAL,
    -- The following field shall not be present if only the kernel is used.
        sender-acse-requirements           [10] IMPLICIT      ACSE-requirements OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.
        mechanism-name                     [11] IMPLICIT      Mechanism-name OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.

        calling-authentication-value       [12] EXPLICIT      Authentication-value OPTIONAL,
        implementation-information         [29] IMPLICIT      Implementation-data OPTIONAL,
        user-information                   [30] EXPLICIT      Association-information OPTIONAL
    }
    >>> aarq = AARQ('60 29 A1 09 06 07 60 85 74 05 08 01 01 A6 0A 04 08 00 00 00 00 00 00 98 00 BE 10 04 0E 01 00 00 00 06 5F 1F 04 00 00 1F 3F FF FD')
    >>> aarq.frame.hex()
    '6029a109060760857405080101a60a04080000000000009800be10040e01000000065f1f0400001f3ffffd'
    >>> aarq.member
    {'protocol-version': (b'\\x80', 1), 'application-context-name': '2.16.756.5.8.1.1', 'calling-AP-title': b'\\x00\\x00\\x00\\x00\\x00\\x00\\x98\\x00', 'user-information': b'\\x01\\x00\\x00\\x00\\x06_\\x1f\\x04\\x00\\x00\\x1f?\\xff\\xfd'}

    {
        'protocol-version': (b'\\x80', 1),
        'application-context-name': '2.16.756.5.8.1.1',
        'calling-AP-title': b'\\x00\\x00\\x00\\x00\\x00\\x00\\x98\\x00',
        'user-information': b'\\x01\\x00\\x00\\x00\\x06_\\x1f\\x04\\x00\\x00\\x1f?\\xff\\xfd'
    }

    >>> aarq = AARQ({ \
        'protocol-version': (b'\\x80', 1), \
        'application-context-name': '2.16.756.5.8.1.1', \
        'calling-AP-title': b'\\x00\\x00\\x00\\x00\\x00\\x00\\x98\\x00', \
        'user-information': b'\\x01\\x00\\x00\\x00\\x06_\\x1f\\x04\\x00\\x00\\x1f?\\xff\\xfd' \
        })
    >>> aarq.member
    {'protocol-version': (b'\\x80', 1), 'application-context-name': '2.16.756.5.8.1.1', 'calling-AP-title': b'\\x00\\x00\\x00\\x00\\x00\\x00\\x98\\x00', 'user-information': b'\\x01\\x00\\x00\\x00\\x06_\\x1f\\x04\\x00\\x00\\x1f?\\xff\\xfd'}
    >>> aarq.frame.hex()
    '6029a109060760857405080101a60a04080000000000009800be10040e01000000065f1f0400001f3ffffd'
    """

    name = 'aarq'

    def __init__(self, data):
        super(AARQ, self).__init__(data)

    def _decode_asn(self):
        self.member = COSEMpdu.decode('ACSE-APDU', self.frame)[1]

    def _encode_asn(self):
        self.frame = COSEMpdu.encode('ACSE-APDU', ('aarq', self.member))


class AARE(COSEMpduMember):
    """
    AARE-apdu ::= [APPLICATION 1] IMPLICIT SEQUENCE
    {
    -- [APPLICATION 1] == [ 61H ] = [ 97 ]

        protocol-version                   [0] IMPLICIT        BIT STRING {version1 (0)} DEFAULT {version1},
        application-context-name           [1]                 Application-context-name,
        result                             [2]                 Association-result,
        result-source-diagnostic           [3]                 Associate-source-diagnostic,
        responding-AP-title                [4]                 AP-title OPTIONAL,
        responding-AE-qualifier            [5]                 AE-qualifier OPTIONAL,
        responding-AP-invocation-id        [6]                 AP-invocation-identifier OPTIONAL,
        responding-AE-invocation-id        [7]                 AE-invocation-identifier OPTIONAL,

    -- The following field shall not be present if only the kernel is used.
        responder-acse-requirements        [8] IMPLICIT        ACSE-requirements OPTIONAL,

    -- The following field shall only be present if the authentication functional unit is selected.
        mechanism-name                     [9] IMPLICIT        Mechanism-name OPTIONAL,

    -- The following field shall only be present if the authentication functional unit is selected.
        responding-authentication-value    [10] EXPLICIT       Authentication-value OPTIONAL,
        implementation-information         [29] IMPLICIT       Implementation-data OPTIONAL,
        user-information                   [30] EXPLICIT       Association-information OPTIONAL
    }

    >>> aare = AARE('61 35 A1 09 06 07 60 85 74 05 08 01 01 A2 03 02 01 00 A3 05 A1 03 02 01 00 A4 0A 04 08 4B 46 4D 67 70 00 00 0C BE 10 04 0E 08 00 06 5F 1F 04 00 00 10 19 04 C8 00 07')
    >>> aare.frame.hex()
    '6135a109060760857405080101a203020100a305a103020100a40a04084b464d677000000cbe10040e0800065f1f040000101904c80007'
    >>> aare.member
    {'protocol-version': (b'\\x80', 1), 'application-context-name': '2.16.756.5.8.1.1', 'result': 0, 'result-source-diagnostic': ('acse-service-user', 0), 'responding-AP-title': b'KFMgp\\x00\\x00\\x0c', 'user-information': b'\\x08\\x00\\x06_\\x1f\\x04\\x00\\x00\\x10\\x19\\x04\\xc8\\x00\\x07'}

    {
        'protocol-version': (b'\x80', 1),
        'application-context-name': '2.16.756.5.8.1.1',
        'result': 0, 'result-source-diagnostic': ('acse-service-user', 0),
        'responding-AP-title': b'KFMgp\x00\x00\x0c',
        'user-information': b'\x08\x00\x06_\x1f\x04\x00\x00\x10\x19\x04\xc8\x00\x07'
    }

    >>> aare = AARE({ \
        'protocol-version': (b'\\x80', 1), \
        'application-context-name': '2.16.756.5.8.1.1', \
        'result': 0, 'result-source-diagnostic': ('acse-service-user', 0), \
        'responding-AP-title': b'KFMgp\\x00\\x00\\x0c', \
        'user-information': b'\\x08\\x00\\x06_\\x1f\\x04\\x00\\x00\\x10\\x19\\x04\\xc8\\x00\\x07' \
        })
    >>> aare.member
    {'protocol-version': (b'\\x80', 1), 'application-context-name': '2.16.756.5.8.1.1', 'result': 0, 'result-source-diagnostic': ('acse-service-user', 0), 'responding-AP-title': b'KFMgp\\x00\\x00\\x0c', 'user-information': b'\\x08\\x00\\x06_\\x1f\\x04\\x00\\x00\\x10\\x19\\x04\\xc8\\x00\\x07'}
    >>> aare.frame.hex()
    '6135a109060760857405080101a203020100a305a103020100a40a04084b464d677000000cbe10040e0800065f1f040000101904c80007'
    """
    name = 'aare'
    def __init__(self, data):
        super(AARE, self).__init__(data)

    def _decode_asn(self):
        self.member = COSEMpdu.decode('ACSE-APDU', self.frame)[1]

    def _encode_asn(self):
        self.frame = COSEMpdu.encode('ACSE-APDU', ('aare', self.member))

class RLRQ(COSEMpduMember):
    """
    AARQ-apdu ::= [APPLICATION 0] IMPLICIT SEQUENCE {
    -- [APPLICATION 0] == [ 60H ] = [ 96 ]

        protocol-version                   [0] IMPLICIT        BIT STRING {version1 (0)}    DEFAULT{version1},
        application-context-name           [1]                 Application-context-name,
        called-AP-title                    [2]                 AP-title OPTIONAL,
        called-AE-qualifier                [3]                 AE-qualifier OPTIONAL,
        called-AP-invocation-id            [4]                 AP-invocation-identifier OPTIONAL,
        called-AE-invocation-id            [5]                 AE-invocation-identifier OPTIONAL,
        calling-AP-title                   [6]                 AP-title OPTIONAL,
        calling-AE-qualifier               [7]                 AE-qualifier OPTIONAL,
        calling-AP-invocation-id           [8]                 AP-invocation-identifier OPTIONAL,
        calling-AE-invocation-id           [9]                 AE-invocation-identifier OPTIONAL,
    -- The following field shall not be present if only the kernel is used.
        sender-acse-requirements           [10] IMPLICIT      ACSE-requirements OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.
        mechanism-name                     [11] IMPLICIT      Mechanism-name OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.

        calling-authentication-value       [12] EXPLICIT      Authentication-value OPTIONAL,
        implementation-information         [29] IMPLICIT      Implementation-data OPTIONAL,
        user-information                   [30] EXPLICIT      Association-information OPTIONAL
    }
    """
    def __init__(self, data):
        super(RLRQ, self).__init__(data)


class RLRE(COSEMpduMember):
    """
    AARQ-apdu ::= [APPLICATION 0] IMPLICIT SEQUENCE {
    -- [APPLICATION 0] == [ 60H ] = [ 96 ]

        protocol-version                   [0] IMPLICIT        BIT STRING {version1 (0)}    DEFAULT{version1},
        application-context-name           [1]                 Application-context-name,
        called-AP-title                    [2]                 AP-title OPTIONAL,
        called-AE-qualifier                [3]                 AE-qualifier OPTIONAL,
        called-AP-invocation-id            [4]                 AP-invocation-identifier OPTIONAL,
        called-AE-invocation-id            [5]                 AE-invocation-identifier OPTIONAL,
        calling-AP-title                   [6]                 AP-title OPTIONAL,
        calling-AE-qualifier               [7]                 AE-qualifier OPTIONAL,
        calling-AP-invocation-id           [8]                 AP-invocation-identifier OPTIONAL,
        calling-AE-invocation-id           [9]                 AE-invocation-identifier OPTIONAL,
    -- The following field shall not be present if only the kernel is used.
        sender-acse-requirements           [10] IMPLICIT      ACSE-requirements OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.
        mechanism-name                     [11] IMPLICIT      Mechanism-name OPTIONAL,
    -- The following field shall only be present if the authentication functional unit is selected.

        calling-authentication-value       [12] EXPLICIT      Authentication-value OPTIONAL,
        implementation-information         [29] IMPLICIT      Implementation-data OPTIONAL,
        user-information                   [30] EXPLICIT      Association-information OPTIONAL
    }
    """
    def __init__(self, data):
        super(RLRE, self).__init__(data)


class InitiateRequest(COSEMpduMember):
    def __init__(self, data):
        super(InitiateRequest, self).__init__(data)


class ReadRequest(COSEMpduMember):
    def __init__(self, data):
        super(ReadRequest, self).__init__(data)


class WriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(WriteRequest, self).__init__(data)


class InitiateResponse(COSEMpduMember):
    def __init__(self, data):
        super(InitiateResponse, self).__init__(data)


class ReadResponse(COSEMpduMember):
    def __init__(self, data):
        super(ReadResponse, self).__init__(data)


class WriteResponse(COSEMpduMember):
    def __init__(self, data):
        super(WriteResponse, self).__init__(data)


class ConfirmedServiceError(COSEMpduMember):
    def __init__(self, data):
        super(ConfirmedServiceError, self).__init__(data)


class DataNotification(COSEMpduMember):
    def __init__(self, data):
        super(DataNotification, self).__init__(data)


class UnconfirmedWriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(UnconfirmedWriteRequest, self).__init__(data)


class InformationReportRequest(COSEMpduMember):
    def __init__(self, data):
        super(InformationReportRequest, self).__init__(data)


class GloInitiateRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloInitiateRequest, self).__init__(data)


class GloReadRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloReadRequest, self).__init__(data)


class GloWriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloWriteRequest, self).__init__(data)


class GloInitiateResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloInitiateResponse, self).__init__(data)


class GloReadResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloReadResponse, self).__init__(data)


class GloWriteResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloWriteResponse, self).__init__(data)


class GloConfirmedServiceError(COSEMpduMember):
    def __init__(self, data):
        super(GloConfirmedServiceError, self).__init__(data)


class GloUnconfirmedWriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloUnconfirmedWriteRequest, self).__init__(data)


class GloInformationReportRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloInformationReportRequest, self).__init__(data)


class DedInitiateRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedInitiateRequest, self).__init__(data)


class DedReadRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedReadRequest, self).__init__(data)


class DedWriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedWriteRequest, self).__init__(data)


class DedInitiateResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedInitiateResponse, self).__init__(data)


class DedReadResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedReadResponse, self).__init__(data)


class DedReadResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedReadResponse, self).__init__(data)


class DedConfirmedServiceError(COSEMpduMember):
    def __init__(self, data):
        super(DedConfirmedServiceError, self).__init__(data)


class DedUnconfirmedWriteRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedUnconfirmedWriteRequest, self).__init__(data)


class DedInformationReportRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedInformationReportRequest, self).__init__(data)


class GetRequest(COSEMpduMember):
    def __init__(self, data):
        super(GetRequest, self).__init__(data)


class SetRequest(COSEMpduMember):
    def __init__(self, data):
        super(SetRequest, self).__init__(data)


class EventNotificationRequest(COSEMpduMember):
    def __init__(self, data):
        super(EventNotificationRequest, self).__init__(data)


class ActionRequest(COSEMpduMember):
    def __init__(self, data):
        super(ActionRequest, self).__init__(data)


class GetResponse(COSEMpduMember):
    def __init__(self, data):
        super(GetResponse, self).__init__(data)


class SetResponse(COSEMpduMember):
    def __init__(self, data):
        super(SetResponse, self).__init__(data)


class ActionResponse(COSEMpduMember):
    def __init__(self, data):
        super(ActionResponse, self).__init__(data)


class GloGetRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloGetRequest, self).__init__(data)


class GloSetRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloSetRequest, self).__init__(data)


class GloEventNotificationRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloEventNotificationRequest, self).__init__(data)


class GloActionRequest(COSEMpduMember):
    def __init__(self, data):
        super(GloActionRequest, self).__init__(data)


class GloGetResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloGetResponse, self).__init__(data)


class GloSetResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloSetResponse, self).__init__(data)


class GloActionResponse(COSEMpduMember):
    def __init__(self, data):
        super(GloActionResponse, self).__init__(data)


class DedGetRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedGetRequest, self).__init__(data)


class DedSetRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedSetRequest, self).__init__(data)


class DedEventNotificationRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedEventNotificationRequest, self).__init__(data)


class DedActionRequest(COSEMpduMember):
    def __init__(self, data):
        super(DedActionRequest, self).__init__(data)


class DedGetResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedGetResponse, self).__init__(data)


class DedSetResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedSetResponse, self).__init__(data)


class DedActionResponse(COSEMpduMember):
    def __init__(self, data):
        super(DedActionResponse, self).__init__(data)


class ExceptionResponse(COSEMpduMember):
    def __init__(self, data):
        super(ExceptionResponse, self).__init__(data)


class AccessRequest(COSEMpduMember):
    def __init__(self, data):
        super(AccessRequest, self).__init__(data)


class AccessResponse(COSEMpduMember):
    def __init__(self, data):
        super(AccessResponse, self).__init__(data)


class GeneralGloCiphering(COSEMpduMember):
    def __init__(self, data):
        super(GeneralGloCiphering, self).__init__(data)


class GeneralDedCiphering(COSEMpduMember):
    def __init__(self, data):
        super(GeneralDedCiphering, self).__init__(data)


class GeneralCiphering(COSEMpduMember):
    def __init__(self, data):
        super(GeneralCiphering, self).__init__(data)


class GeneralSigning(COSEMpduMember):
    def __init__(self, data):
        super(GeneralSigning, self).__init__(data)


class GeneralBlockTransfer(COSEMpduMember):
    def __init__(self, data):
        super(GeneralBlockTransfer, self).__init__(data)


if __name__ == '__main__':
    aarq = AARQ({'protocol-version': (b'\x80', 1), 'application-context-name': '2.16.756.5.8.1.1',
                           'calling-AP-title': b'\x00\x00\x00\x00\x00\x00\x98\x00',
                           'user-information': b'\x01\x00\x00\x00\x06_\x1f\x04\x00\x00\x1f?\xff\xfd'}
                )
    print(aarq.__dict__)