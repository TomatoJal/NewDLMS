import asn1

COSEMpdu = asn1.compile_files(r'E:\OnePiece\Project\0007.KFM\NewDLMS\COSEMpdu\COSEMpdu.asn')
                              # cache_dir='E:\\OnePiece\\Project\\0007.KFM\\NewDLMS\\COSEMpdu\\')


aarq_frame = bytearray([0x60, 0x29, 0xA1, 0x09, 0x06, 0x07, 0x60, 0x85, 0x74, 0x05, 0x08, 0x01, 0x01, 0xA6, 0x0A, 0x04,
                        0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x98, 0x00, 0xBE, 0x10, 0x04, 0x0E, 0x01, 0x00, 0x00,
                        0x00, 0x06, 0x5F, 0x1F, 0x04, 0x00, 0x00, 0x1F, 0x3F, 0xFF, 0xFD])
aarq_decode = COSEMpdu.decode('ACSE-APDU', aarq_frame)
print(aarq_decode)


aarq_encoded = COSEMpdu.encode('AARQ-apdu', {
    'application-context-name': '2.16.756.5.8.1.1',
    'calling-AP-title': b'\x00\x00\x00\x00\x00\x00\x98\x00',
    'user-information': b'\x01\x00\x00\x00\x06_\x1f\x04\x00\x00\x1f?\xff\xfd'
})
print(aarq_encoded.hex())
print(aarq_frame.hex())
