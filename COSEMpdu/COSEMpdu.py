from asn1 import *


class COSEMpdu:
    def __init__(self,
                 filenames,
                 codec='ber',
                 any_defined_by_choices=None,
                 encoding='utf-8',
                 cache_dir=None,
                 numeric_enums=False):
        self.COSEMpdu = compile_files(filenames, codec, any_defined_by_choices, encoding, cache_dir, numeric_enums)

    def decode(self, name, data, check_constraints=False):
        # data 数据类型转换



        return self.COSEMpdu.decode(name, data, check_constraints)
        try:
            return self.COSEMpdu.decode(name, data, check_constraints)
        except:
            for member in self.COSEMpdu.types[name].type.members:
                if data[0] == member.decode_tag(member.tag):
                    return member
            return None

    def encode(self,
               name,
               data,
               check_types=True,
               check_constraints=False,
               **kwargs):
        pass

COSEMpdu = COSEMpdu(r'E:\OnePiece\Project\0007.KFM\NewDLMS.git\COSEMpdu\COSEMpdu.asn',
                    cache_dir=r'E:\OnePiece\Project\0007.KFM\NewDLMS.git\COSEMpdu\cache')




