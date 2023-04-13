from sqlalchemy import create_engine
db_conn_string = "mysql+pymysql://vrx1wcrzgwp4k3s7crjm:pscale_pw_HcpzTSwQTu0Wat0uNaM3eJFA2TBy7l42dvl0ukqmLiL@aws.connect.psdb.cloud/career_website?charset=utf8mb4"

engine = create_engine(
    db_conn_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
) 

