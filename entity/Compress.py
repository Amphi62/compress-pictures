from datetime import datetime
from PIL import Image
from utility.files import *
import os


class Compress:
    def __init__(self, list_files, quality=50, extensions='.jpeg,.jpg,.gif,.png', copy_active=False,
                 in_her_directory=False):
        """
        :param list_files: list files or folders to treatment
        :param quality: quality of compressing, default 50
        :param extensions: extension files will be concerned, default jpeg, jpg, gif and png
        :param copy_active: copy all other files to reproduce the target folder, default false
        :param in_her_directory: create the compress folder in the same directory of the target, default false
            he will create the compress folder in the root of compress project
        """
        self.__list_files = list_files

        self.__quality = quality
        self.__extensions = extensions
        self.__copy_active = copy_active
        self.__in_her_directory = in_her_directory

        format_date = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.__header_name = f'compress_images_{format_date}'

    def execute(self):
        for files in self.__list_files:
            files_name = build_name(files)

            if os.path.isfile(files):
                self.is_file_treatment(files, f'{self.__header_name}_{files_name}')
            elif os.path.isdir(files):
                self.is_folder_treatment(files, files_name, True)
            else:
                raise Exception('Chemin pas trouvable...')

    def is_file_treatment(self, file: str, file_name: str):
        if self.in_list_extensions(file):
            self.create_compress_file(file, file_name)

    def is_folder_treatment(self, directory: str, directory_name: str, is_first=False):
        if is_first:
            directory_name = f'{self.__header_name}_{directory_name}'

            if self.__in_her_directory:
                directory_name = f'{get_start_url(directory)}/{directory_name}'

        os.mkdir(directory_name)

        for child in os.listdir(directory):
            element = f'{directory}/{child}'

            if child != '.' and child != '..':
                if os.path.isdir(element):
                    self.is_folder_treatment(element, f'{directory_name}/{child}')
                elif os.path.isfile(element):
                    self.is_file_treatment(element, f'{directory_name}/{child}')

    def in_list_extensions(self, file: str) -> bool:
        """
        Check if the file have an extension corresponding who want to treat
        :param file: url file
        :return: True if the extension corresponding, else False
        """
        for extension_file in self.__extensions:
            if file.endswith(extension_file):
                return True
        return False

    def create_compress_file(self, url_file: str, url_generate_file: str):
        """
        Generate a compress file
        :param url_file: url file of original files who want to compress
        :param url_generate_file: url destination
        :return: None
        """
        if self.__in_her_directory:
            path = get_start_url(url_file)
            url_generate_file = f'{path}/{url_generate_file}'

        picture = Image.open(url_file)
        picture = picture.resize(picture.size, Image.ANTIALIAS)
        picture.save(url_generate_file, optimize=True, quality=self.__quality)
