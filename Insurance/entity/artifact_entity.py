from dataclasses import dataclass

class DataIngestionartifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str