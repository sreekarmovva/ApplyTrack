from database import get_connection


def get_all_applications():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM applications")
            rows = cur.fetchall()

    return rows

def add_applications(company, role, status):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
            INSERT INTO applications (company, role, status)
            VALUES (%s,%s,%s)
            RETURNING id
            """,
            (company, role, status)
            )

            application_id = cur.fetchone()[0]


        return application_id    
    