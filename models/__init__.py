# from .engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
