from etl.ingest import load_csv
from etl.normalize import clean_name, clean_date
from ai.enrich import ai_enrich
from db.database import init_db, get_connection

def main():
    init_db()
    df = load_csv("data/members_raw.csv")

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        name = clean_name(row.get("Name"))
        dob = clean_date(row.get("DOB"))
        bio = row.get("Bio_or_comment")

        if not name or not dob:
            continue

        cursor.execute(
            "INSERT INTO members (name, dob, status) VALUES (?, ?, ?)",
            (name, dob, "processed")
        )
        member_id = cursor.lastrowid

        ai_data = ai_enrich(bio)

        cursor.execute(
            "INSERT INTO persona VALUES (?, ?, ?)",
            (member_id, ai_data["persona"], ai_data["confidence"])
        )

        for skill in ai_data["skills"]:
            cursor.execute(
                "INSERT OR IGNORE INTO skills (name) VALUES (?)",
                (skill,)
            )
            cursor.execute(
                "SELECT id FROM skills WHERE name = ?",
                (skill,)
            )
            skill_id = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO member_skills VALUES (?, ?)",
                (member_id, skill_id)
            )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

