import environs

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = environs.Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PEAR_URL = '''https://fruitonline.ru/fruits/pear'''
APPLE_URL = '''https://fruitonline.ru/search?search=яблоко'''
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
POSTGRESURI = f'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'