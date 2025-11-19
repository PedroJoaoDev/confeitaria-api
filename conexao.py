import psycopg2

load_dotenv()

def get_conexao():
    conn =  psycopg2.connect(
        dbname = os.getenv('postgres'),
        user = os.getenv('postgres.clxalkgiugazshfvqjln'),
        password = os.getenv('Jp101627.'),
        host = os.getenv('aws-1-us-east-2.pooler.supabase.com'),
        port = os.getenv('6543')
    )
    return conn