import importlib
import pathlib

from aiogram.dispatcher import Dispatcher


class LoadingClasses:
    def __init__(self, folder):
        self.folder = folder
        self.list = list()
        self.current_directory = pathlib.Path(folder)
        self.ignor_file = list()

    def load_classes(self):
        for current_file in self.current_directory.glob('*.py'):
            self.ignor_file.append('__init__.py')
            if current_file.name not in self.ignor_file:
                file = current_file.name.replace('.py', '')
                module = importlib.import_module(f"{self.folder}.{file}")
                my_class = getattr(module, file)
                self.list.append(my_class)


class LoadingModule(LoadingClasses):
    def __init__(self, folder=None):
        if not folder:
            folder = 'modules'
        super(LoadingModule, self).__init__(folder)

    def load_modules(self, dp, loop):
        self.load_classes()
        for class_ in self.list:
            classes = class_(dp, loop)

            if 'register_handlers' in dir(classes):
                classes.register_handlers()


class LoadingFilters(LoadingClasses):
    def __init__(self, folder=None):
        if not folder:
            folder = 'filters'
        super(LoadingFilters, self).__init__(folder)

    def load_filters(self, dp: Dispatcher):
        self.load_classes()
        for class_ in self.list:
            dp.filters_factory.bind(class_)

