import ntpath

from dropbox import dropbox as dbx


# Dropbox #
class Dropbox:
    def __init__(self, api_key: str):
        self.db = dbx.Dropbox(api_key)

    def download_file(self, filePath, toWhere=None) -> bool:
        try:
            if toWhere:
                self.db.files_download_to_file(f'/{filePath}', toWhere)
            else:
                self.db.files_download('/{}'.format(filePath))
            return True
        except FileNotFoundError:
            pass
        return False

    def upload_file(self, filePath, rename=False) -> bool:
        try:
            with open(filePath, 'rb') as f:
                if not rename:
                    filename = ntpath.basename(filePath)
                self.db.files_upload(f.read(), f'/{(rename if rename else filename)}',
                                     mode=dbx.files.WriteMode('overwrite'))
            return True
        except:
            pass
        return False

    def check_if_folder_exists(self, folderPath) -> bool:
        try:
            self.db.files_get_metadata(f'/{folderPath}')
            return True
        except:
            pass
        return False

    def create_folder_path(self, folderPath) -> bool:
        """
        Ex. Create /home/2020/Spring folders
        """
        try:
            folders = folderPath.split('/')
            from_root = ""
            for folder in folders:
                if not self.check_if_folder_exists(f"{from_root}{folder}"):
                    self.db.files_create_folder_v2(f"/{from_root}{folder}")
                from_root += folder + "/"
            return True
        except:
            pass
        return False
