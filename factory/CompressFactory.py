from entity.Compress import Compress
from utility.command import check_is_option, check_next_is_ok, get_quality, extension


class CompressFactory:
    @staticmethod
    def build(list_arg):
        quality = 50
        files_extensions = ['.jpeg', '.jpg', '.png', '.gif']
        list_files_folders = []
        i = 0

        while i < len(list_arg):
            if check_is_option(list_arg[i]):  # is an option
                if list_arg[i] == '-q':  # quality option
                    if check_next_is_ok(list_arg, i):
                        i += 1
                        quality = get_quality(list_arg[i])
                    else:
                        raise Exception('L\'argument -q nécessite une valeur derrière elle !')
                elif list_arg[i] == '-e':
                    if check_next_is_ok(list_arg, i):
                        i += 1
                        files_extensions = list(map(extension, list_arg[i].split(',')))
                    else:
                        raise Exception('L\'argument -e nécessite une valeur derrière elle !')
                else:
                    raise Exception('L\'option saisi n\'existe pas...')
            else:
                list_files_folders.append(list_arg[i])

            i += 1

        if len(list_files_folders) == 0:
            raise Exception('Il faut au minimum un fichier ou un dossier ...')

        return Compress(
            list_files_folders,
            quality=quality,
            extensions=files_extensions
        )
