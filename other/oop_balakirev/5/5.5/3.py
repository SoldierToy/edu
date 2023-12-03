class PrimaryKey:
    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            print('выход')
        except Exception(ValueError):
            pass


with PrimaryKey() as pk:
    raise ValueError
