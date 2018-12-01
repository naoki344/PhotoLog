from enum import Enum
import os


class FileID:
    def __init__(self, value):
        self.value = value


class Name:
    def __init__(self, value):
        self.value = value


class Path:
    def __init__(self, value):
        self.value = value


class StorageType(Enum):
    LOCAL_DIRECTORY = 1
    AWS_S3_STRAGE = 2


class Location:
    def __init__(self, storage_type: StorageType, path: Path):
        self.storage_type = storage_type
        self.path = path

    @staticmethod
    def from_dict(dict_data):
        return Location(StorageType[dict_data['storage_type']],
                        Path(dict_data['path']))


class Width:
    def __init__(self, width):
        self.value = width


class Height:
    def __init__(self, height):
        self.value = height


class ShapeSize:
    def __init__(self, width: Width, height: Height):
        self.width = width
        self.height = height

    @staticmethod
    def from_dict(dict_data):
        return ShapeSize(
            width=Width(dict_data['width']),
            height=Height(dict_data['height']))

    def to_dict(self):
        return {
            "width": self.width.value,
            "height": self.height.value,
        }


class FileType(Enum):
    # 分類コード(1)  拡張子コード(001) # 表示形式コード(01)
    gif = 100101
    jpg = 100201
    JPG = 100202
    jpe = 100203
    jpeg = 100204
    JPEG = 100205
    jfi = 100204
    png = 100301
    bmp = 100401
    dib = 100402
    rle = 100403
    ico = 100501
    ai = 100601
    art = 100602
    cam = 100701
    cdr = 100801
    cgm = 100901
    cmp = 101001
    dpx = 101101
    fal = 101201
    q0 = 101301
    fpx = 101401
    j6i = 101501
    mac = 101601
    mag = 101701
    maki = 101702
    mng = 101801
    pcd = 101901
    pct = 102001
    pic = 102002
    pict = 102003
    pcx = 102101
    pmp = 102201
    pnm = 102202
    psd = 102301
    ras = 102401
    sj1 = 102501
    tif = 102601
    tiff = 102602
    nsk = 102603
    tga = 102701
    wmf = 102801
    wpg = 102901
    xbm = 103001
    xpm = 103101

    @staticmethod
    def get_by_name(name: Name):
        base, ext = os.path.splitext(name.value)
        ext = ext.replace('.', '')
        return FileType[ext]

    # 拡張子	説明
    # .gif	★ GIFファイル。画像ファイル。Graphics Interchange Format の略。インターネットで JPEG と並んで最も広く使用されている画像フォーマット。Unisys社の特許を使用しているためにフリーソフトがほとんど存在しないのが難点。MIMEタイプは image/gif。
    # .jpg
    # .jpeg
    # .jpe
    # .jfif	★ JPEGファイル。画像ファイル。Joint Photographic Experts Group の略。標準化を行ったグループの名前がそのまま画像フォーマットの名前になっている。ウェブページではGIFとJPEGが両横綱としてよく使用されている。アイコンなど色数の少ないものはGIF、写真など色数の多いものはJPEGが適している。MIMEタイプは image/jpeg。
    # .png	★ PNGファイル。画像ファイル。GIF画像でUnisysの特許問題があることから、GIFに代わるフォーマットして定められた画像ファイル形式。「ピング」と読む。HTMLなどの標準化を行っている団体 W3C が規定。Internet Explorer 4.0、Netscape Communicator 4.04 以降で対応。MIMEタイプは image/png。
    # .bmp
    # .dib
    # rle	★ Windows 標準のビットマップファイル。BMP（BitMaP）、DIB（Device Independent Bitmap）。「ペイント」で作成した画像は通常BMPファイルとして保存される。ファイルサイズが大きいため、インターネット上での使用には適していない。
    # .ico	★ アイコンファイル。Windowsのアイコン用画像ファイル。ビットマップファイル（.bmp）の拡張子を .ico に変更しただけでも使用できる場合があるが、通常は別物。専用のアイコンエディタで作成する。
    # .ai
    # .art	Adobe Illustratorファイル。
    # .cam	QV-10 などのデジタルカメラで使用されるフォーマット。
    # .cdr	CorelDraw Drawing ファイル。
    # .cgm	Computer Graphic Metafile ファイル。
    # .cmp	LEADファイル。
    # .dpx	DOIChan!氏開発のフリーソフト D-Pixed のフォーマット。
    # .fal
    # .q0	Nifty-Serve の FPICS フォーラムで開発されたフォーマット。
    # .fpx	Kodak社の Flash Pix ファイル。
    # .j6i	DC-1 など、オリンパスやリコーのデジタルカメラで使用。
    # .mac	MacPaint ファイル。
    # .mag
    # .maki	MAKIフォーマット。通称「まきちゃんフォーマット」
    # .mng	動画対応版 PNGフォーマット。
    # .pcd	Kodak社の PhotoCD ファイル。
    # .pct
    # .pic
    # .pict	PICTファイル。Macintoshでよく用いられていた画像形式。
    # .pcx	ZSoft社の PC Paintbrush 用ファイル。
    # .pmp	Cyber-Shot などのデジタルカメラで使用されるフォーマット。
    # .pnm	PNMPLUS フォーマット。
    # .psd	Adobe社 PhotoShop のファイル。
    # .ras	Sun のラスタ（raster）ファイル。
    # .sj1	DIGIO などのデジタルカメラで使用されるフォーマット。
    # .tif
    # .tiff
    # .nsk	TIFF（Tagged Image File Format）ファイル。画像ファイル。Aldus社（現在は Adobe社に吸収）が開発した画像形式。
    # .tga	Truevision TARGA ファイル。
    # .wmf	Microsoft社の WMF（Windows Meta File）形式ファイル。
    # .wpg	WordPerfect のファイル。
    # .xbm	W-Window のビットマップ。
    # .xpm	W-Window のパレット付き画像ファイル。


'''
Value Object : LastUpdateDate
'''


class LastUpdateDate:
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


'''
Value Object : RegisterDate
'''


class RegisterDate:
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


class File:
    def __init__(self, file_id: FileID, name: Name, location: Location,
                 file_type: FileType, shape_size: ShapeSize,
                 register_date: RegisterDate,
                 last_update_date: LastUpdateDate):
        self.file_id = file_id
        self.name = name
        self.location = location
        self.file_type = file_type
        self.shape_size = shape_size
        self.register_date = register_date
        self.last_update_date = last_update_date

    def to_dict(self):
        return {
            'file_id': self.file_id.value,
            'name': self.name.value,
            'url': self._get_url(),
            'file_type': self.file_type.name,
            'shape_size': self.shape_size.to_dict(),
            'register_date': self.register_date.datetime_string(),
            'last_update_date': self.last_update_date.datetime_string(),
        }

    @staticmethod
    def from_dict(dict_data: dict) -> 'File':
        return File(
            file_id=FileID(dict_data['file_id']),
            name=Name(dict_data['name']),
            location=Location.from_dict(dict_data),
            file_type=FileType[dict_data['file_type']],
            shape_size=ShapeSize.from_dict(dict_data),
            register_date=RegisterDate(dict_data['register_date']),
            last_update_date=LastUpdateDate(dict_data['last_update_date']),
        )

    def _get_url(self):
        return '/file/strage/{}'.format(self.file_id.value)
